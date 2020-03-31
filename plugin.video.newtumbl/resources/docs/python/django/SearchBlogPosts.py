from django.db import models
'''
https://api-ro.newtumbl.com/sp/NewTumbl/search_Blog_Posts
fetch("https://api-ro.newtumbl.com/sp/NewTumbl/search_Blog_Posts", {"credentials":"omit","headers":{"accept":"*/*","content-type":"application/x-www-form-urlencoded; charset=UTF-8","sec-fetch-mode":"cors"},"referrer":"https://1of2dads.newtumbl.com/","referrerPolicy":"no-referrer-when-downgrade","body":"json=%7B%22Params%22%3A%5B%22%5B%7BIPADDRESS%7D%5D%22%2C%22FzCWMJIw6mi8gl6pU6LgpGMcncAg75JIqnqBsiGK2tytG76I%22%2C391932%2Cnull%2Cnull%2C0%2C50%2C0%2Cnull%2C0%2C%22%22%2C0%2C0%2C0%2C0%2C0%2C30142%2Cnull%5D%7D","method":"POST","mode":"cors"});
curl 'https://api-ro.newtumbl.com/sp/NewTumbl/search_Blog_Posts' -H 'Accept: */*' -H 'Referer: https://1of2dads.newtumbl.com/' -H 'DNT: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' -H 'Sec-Fetch-Mode: cors' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' --data 'json=%7B%22Params%22%3A%5B%22%5B%7BIPADDRESS%7D%5D%22%2C%22FzCWMJIw6mi8gl6pU6LgpGMcncAg75JIqnqBsiGK2tytG76I%22%2C391932%2Cnull%2Cnull%2C0%2C50%2C0%2Cnull%2C0%2C%22%22%2C0%2C0%2C0%2C0%2C0%2C30142%2Cnull%5D%7D' --compressed
Request Parameters
json=%7B%22Params%22%3A%5B%22%5B%7BIPADDRESS%7D%5D%22%2C%22FzCWMJIw6mi8gl6pU6LgpGMcncAg75JIqnqBsiGK2tytG76I%22%2C391932%2Cnull%2Cnull%2C0%2C50%2C0%2Cnull%2C0%2C%22%22%2C0%2C0%2C0%2C0%2C0%2C30142%2Cnull%5D%7D
json: {"Params" : [
    "[{IPADDRESS}]",
    "FzCWMJIw6mi8gl6pU6LgpGMcncAg75JIqnqBsiGK2tytG76I",
    391932,
    null,
    null,
    0,
    50,
    0,
    null,
    0,
    "",
    0,
    0,
    0,
    0,
    0,
    30142,
    null
    ]}
'''

class ARow(models.Model):
	dt_search = models.CharField(max_length=255, blank=True)
	b_part_type_ix = models.FloatField(blank=True)
	dw_blog_ix = models.FloatField(blank=True)
	b_primary = models.FloatField(blank=True)
	n_count_post = models.FloatField(blank=True)
	qw_media_ix_icon = models.FloatField(blank=True)
	b_status = models.FloatField(blank=True)
	sz_u_r_l = models.CharField(max_length=255, blank=True)
	dw_blog_ix_submit = models.FloatField(blank=True)
	dw_blog_ix_orig = models.FloatField(blank=True)
	b_tier = models.FloatField(blank=True)
	qw_media_ix = models.FloatField(blank=True)
	b_order = models.FloatField(blank=True)
	b_state = models.FloatField(blank=True)
	dw_user_ix = models.FloatField(blank=True)
	qw_media_ix_background = models.FloatField(blank=True)
	dw_blog_ix_from = models.FloatField(blank=True)
	b_follow = models.FloatField(blank=True)
	dt_created = models.CharField(max_length=255, blank=True)
	b_block = models.FloatField(blank=True)
	qw_post_ix = models.FloatField(blank=True)
	b_post_type_ix = models.FloatField(blank=True)
	n_part_iz = models.FloatField(blank=True)
	sz_sub = models.CharField(max_length=255, blank=True)
	qw_post_ix_orig = models.FloatField(blank=True)
	sz_title = models.CharField(max_length=255, blank=True)
	b_media_type_ix = models.FloatField(blank=True)
	a_result_set = models.ForeignKey("AResultSet", blank=True)
	sz_tag = models.CharField(max_length=255, blank=True)
	n_count_comment = models.FloatField(blank=True)
	dt_active = models.CharField(max_length=255, blank=True)
	b_private = models.FloatField(blank=True)
	sz_body = models.CharField(max_length=255, blank=True)
	dw_i_p_address_ix = models.FloatField(blank=True)
	qw_post_ix_from = models.FloatField(blank=True)
	n_count_mark = models.FloatField(blank=True)
	b_rating_ix = models.FloatField(blank=True)
	sz_description = models.CharField(max_length=255, blank=True)
	n_height = models.FloatField(blank=True)
	b_icon_shape = models.FloatField(blank=True)
	a_row = models.CharField(max_length=255, blank=True)
	sz_external = models.CharField(max_length=255, blank=True)
	dw_color_foreground = models.FloatField(blank=True)
	n_size = models.FloatField(blank=True)
	dt_scheduled = models.CharField(max_length=255, blank=True)
	dw_checksum = models.FloatField(blank=True)
	b_no_index = models.FloatField(blank=True)
	sz_source = models.CharField(max_length=255, blank=True)
	n_width = models.FloatField(blank=True)
	b_hide = models.FloatField(blank=True)
	n_count_like = models.FloatField(blank=True)
	dw_color_background = models.FloatField(blank=True)
	sz_blog_id = models.CharField(max_length=255, blank=True)
	qw_media_ix_banner = models.FloatField(blank=True)


class AField(models.Model):
	o_min = models.CharField(max_length=255, blank=True)
	o_max = models.CharField(max_length=255, blank=True)
	s_name = models.CharField(max_length=255, blank=True)
	s_type = models.CharField(max_length=255, blank=True)
	b_numeric = models.BooleanField(blank=True, null=True)
	a_result_set = models.ForeignKey("AResultSet", blank=True)


class BlogPosts(models.Model):
	n_result = models.CharField(max_length=255, blank=True)


class AResultSet(models.Model):
	blog_posts = models.ForeignKey("BlogPosts", blank=True)
	n_total_rows = models.FloatField(blank=True)

