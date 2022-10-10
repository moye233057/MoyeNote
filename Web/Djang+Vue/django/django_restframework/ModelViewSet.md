一、概念
使用ModelViewSet作为视图类的父类时，会自带四种操作表的方法
分别是:get、get{id}、post、put、delete
对应覆盖名称为:list、retrieve、create、update、destroy
注意参数都为:(self, request, *args, **kwargs)

请求 	url	                          对应方法	   备注
get	    127.0.0.1:8000/projects/ 	  list	      ListModelMixin
get	    127.0.0.1:8000/projects/{1}/  retrieve	  ....Mixin
post	127.0.0.1:8000/projects/ 	  create	  ....Mixin
put	    127.0.0.1:8000/projects/{1}/  update	  ....Mixin
detete	127.0.0.1:8000/projects/{1}/  destroy	  ....Mixin
get	    127.0.0.1:8000/projects/      useraction  useraction	自定义
post	127.0.0.1:8000/projects/      useraction  useraction	自定义
