from django import template
from chat.models import Post


class LatestPostsNode(template.Node):
    def render(self,context):
        context["latest_posts"] = Post.objects.all().order_by("?","creation_date")
        return ''
        #The render() method is where the work actually happens.


def get_latest_posts(parser,token):
    #token.content has the raw value({}) in the {% {} %}
    return LatestPostsNode()

register = template.Library()
register.tag('latest_post_tag',get_latest_posts)
