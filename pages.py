import web

urls = (
    "/", "home",
    "/pages", "pages",
    "/pages/([0-9]+)", "page",
)

db = web.database(dbn='sqlite', db='WPTX.db')
render = web.template.render("templates/", base="base")

class home:
    def GET(self):
        return render.home()

class pages:
    def GET(self):
        return render.pages(db.select("page"))

class page:
    def GET(self, id):
        pages = db.select("page", dict(id=id), where="id = $id", limit=1)
        pages = list(pages)
        if len(pages) == 0:
            web.notfound()
            return render.notfound("Page with id #%d not found" % int(id))
        return render.page(pages[0])

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()