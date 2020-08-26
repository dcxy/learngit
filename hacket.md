### Git tag

ÿ����һ���汾��ͨ�����ڰ汾���д�һ��tag���������Խ����tag�汾ȡ������tag��branch���ƣ�ֻ��branch�����ƶ�����tag�����ƶ���

#### 1���鿴tag
* �鿴����tag
`git tag`

* �鿴ĳ��tag
`git show [tag-name]`

#### 2���½�tag
* ������tag��Ĭ��tag�Ǵ��������ύ��commit��
`git tag [tag-name]`

* ����ע��tag
`git tag -a [tag-name] -m "tag message"`

* ����׷��tag,����һ������v1.0.0��tag
`git tag v1.0.0 1b2e1d63ff`

`1b2e1d63ff`������Ҫ��ǵ��ύ ID ��ǰ 10 λ�ַ���ͨ��git log��ȡ�ύID����Ҳ�����ø��ύ ID ����һЩ��ǰ��λ��ֻҪ����Ψһ�ġ�

* ɾ��tag
`git tag -d [tag-name]`


#### 3��push��Զ��
* pushһ��tag
```
git push origin <tagname>
```

* һ��������ȫ����δ���͵�Զ�̵ı���tag
```
git push origin --tags
```

* ɾ��Զ��tag����ɾ�����أ���push
```
git tag -d v1.1
git push origin :refs/tags/v1.1
```
![](index_files/8e00ef0d-e2d9-453c-90b2-dbe223fd9132.png)

