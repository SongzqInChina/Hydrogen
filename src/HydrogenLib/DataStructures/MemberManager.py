from ..Classes.Namespace import Namespace
from ..Classes.Auto import AutoCreateDict, AutoCompareClass


class BaseStruct(AutoCompareClass):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return self.name == other


class Infomation(Namespace):
    ...


class User(BaseStruct):
    def __init__(self, name):
        super().__init__(name)
        self.info = Infomation()
        self.groups = set()
        self.domains = set()


class Group(BaseStruct):
    def __init__(self, name):
        super().__init__(name)
        self.info = Infomation()
        self.users = set()
        self.domains = set()


class Domain(BaseStruct):
    def __init__(self, name):
        super().__init__(name)
        self.info = Infomation()
        self.users = set()
        self.groups = set()


priority_dict = {
    "User": 0,
    "Group": 1,
    "Domain": 2,
    User: 0,
    Group: 1,
    Domain: 2
}


class Manager:
    def __init__(self, users=None, groups=None, domains=None):
        self.objects = AutoCreateDict()
        if users is not None:
            for user in users:
                self.add_user(user)
        if groups is not None:
            for group in groups:
                self.add_group(group)

        if domains is not None:
            for domain in domains:
                self.add_domain(domain)

    def add_user(self, user: User) -> bool:
        if user.name in self.objects:
            return False
        self.objects[user.name] = user
        return True

    def remove_user(self, user: User) -> bool:
        if user.name not in self.objects:
            return False
        del self.objects[user.name]
        return True

    def add_group(self, group: Group) -> bool:
        if group.name in self.objects:
            return False
        self.objects[group.name] = group
        return True

    def remove_group(self, group: Group) -> bool:
        if group.name not in self.objects:
            return False
        del self.objects[group.name]
        return True

    def add_domain(self, domain: Domain) -> bool:
        if domain.name in self.objects:
            return False
        self.objects[domain.name] = domain
        return True

    def remove_domain(self, domain: Domain) -> bool:
        if domain.name not in self.objects:
            return False
        del self.objects[domain.name]
        return True

    _ContainerType = Group | Domain
    _NonTopType = User | Group

    def let_join(self, name, container):
        nontop_obj = self.objects[name]
        container_obj = self.objects[container]
        if not isinstance(container_obj, self._ContainerType):
            raise TypeError(f'{container_obj} is not a container')
        if not isinstance(nontop_obj, self._NonTopType):
            raise TypeError(f'{nontop_obj} is not a non-top object')
        if priority_dict[type(nontop_obj)] > priority_dict[type(container_obj)]:
            raise TypeError(f'{nontop_obj} is not a {container_obj}')
        # TODO: 完成容器加入操作， 完成容器离开操作
