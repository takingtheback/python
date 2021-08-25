import myPack.service
myPack.service.addArticle()


# as service 가 없으면 myPack.service.addArticle() 로 작성해도 됨
import myPack.service as service
service.addArticle()
service.delArticle()
service.getArticle()
service.editArticle()


from myPack.service import addArticle
addArticle()