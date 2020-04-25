from flask import render_template,url_for,flash, redirect,request,Blueprint
from flask_login import current_user,login_required
from puppycompanyblog import db
from puppycompanyblog.models import BlogPost,BeerEntry
from puppycompanyblog.blog_posts.forms import BlogPostForm,BeerEntryForm

beerTable = []

blog_posts = Blueprint('blog_posts',__name__)

@blog_posts.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id      )
        db.session.add(blog_post)
        db.session.commit()
        flash("Blog Post Created")
        return redirect(url_for('core.index'))
    return render_template('create_post.html',form=form)

# int: makes sure that the blog_post_id gets passed as in integer
# instead of a string so we can look it up later.
@blog_posts.route('/decider',methods=['GET','POST'])
def blog_post():
    form = BeerEntryForm()
    global beerTable
    # print(beerTable)
    # for beer in beerTable:
    #     print(beer.model)
    # if delete:
    #     beerTable = []
    #     delete = True
    if form.validate_on_submit():
        beerTable.append(BeerEntry(man=form.man.data,
                            model=form.model.data,
                            alc=form.alc.data,
                            volume=form.volume.data,
                            quantity=form.quantity.data,
                            price=form.price.data    )
                        )
        print('Submit success')
        beerTable.sort(key=lambda x: x.eff, reverse=True)
        return redirect(url_for('blog_posts.blog_post',form=form,beerTable=beerTable))
    return render_template('blog_post.html',form=form,beerTable=beerTable)

@blog_posts.route('/decider/delete',methods=['GET'])
def blog_post_delete():
    global beerTable
    print(beerTable)
    beerTable = []
    return redirect(url_for('blog_posts.blog_post'))

@blog_posts.route("/decider/delete/<int:idx>", methods=['GET'])
def blog_post_delete_one(idx):
    global beerTable
    beerTable.pop(idx-1)
    return redirect(url_for('blog_posts.blog_post'))


# @blog_posts.route('/deciderr',methods=['GET','POST'])
# def blog_post_delete():
#     count = 0
#     beerTable = []
#     form = BeerEntryForm()
#     # for beer in beerTable:
#     #     print(beer.model)
#     if form.validate_on_submit():
#         beerTable.append(BeerEntry(man=form.man.data,
#                             model=form.model.data,
#                             alc=form.alc.data,
#                             volume=form.volume.data,
#                             quantity=form.quantity.data,
#                             price=form.price.data    )
#                         )
#         print('Submit success')
#         beerTable.sort(key=lambda x: x.eff, reverse=True)
#         return redirect(url_for('blog_posts.blog_post'))
#     else:
#         print(form.errors)
#     return render_template('blog_post.html',form=form,beerTable=beerTable)

@blog_posts.route("/<int:blog_post_id>/update", methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        # Forbidden, No Access
        abort(403)

    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.text = form.text.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))
    # Pass back the old blog post information so they can start again with
    # the old text and title.
    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text
    return render_template('create_post.html', title='Update',
                           form=form)


@blog_posts.route("/<int:blog_post_id>/delete", methods=['POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)
    db.session.delete(blog_post)
    db.session.commit()
    flash('Post has been deleted')
    return redirect(url_for('core.index'))
