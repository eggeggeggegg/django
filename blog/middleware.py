from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class BlockedIPSMiddleware(MiddlewareMixin):
    """中间件类"""
    allow_ip = ['127.0.0.1']

    # 注意中间件类名可以自己定义，但是中间件函数名process_view必须是这个，不能自己修改
    # 此中间件函数的作用：禁止指定的ip地址访问我们的网站（所有视图都不可以访问）
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """在视图函数调用之前会被调用"""
        user_ip = request.META.get("REMOTE_ADDR")
        path_url = request.path_info
        print(user_ip, path_url)
        if path_url != '/admin/':
            return
        if user_ip in self.allow_ip:
            return
        return HttpResponse('forbid')
