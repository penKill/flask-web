-- auto-generated definition
create table t_button
(
	id bigint auto_increment
		primary key,
	menu_id bigint null comment '对应的菜单id',
	word varchar(200) null comment '页面的按钮',
	note varchar(200) null comment '按钮说明'
)
comment '按钮表';

create table t_button_role
(
	id bigint auto_increment
		primary key,
	role_id bigint not null,
	button_id bigint not null,
	create_time timestamp null
)
comment '角色按钮表';

create table t_menu
(
	id bigint auto_increment
		primary key,
	note varchar(200) null comment '文本信息',
	parent_id bigint not null comment '父节点id',
	create_time datetime null comment '创建时间',
	update_time datetime null comment '修改时间',
	path varchar(200) null comment '路径信息'
)
comment '菜单表';

create table t_menu_role
(
	id bigint auto_increment
		primary key,
	role_id bigint not null,
	menu_id bigint not null,
	create_time timestamp null
)
comment '角色按钮联动表';

create table t_role
(
	id bigint auto_increment
		primary key,
	role_name varchar(200) null comment '角色名称',
	company_id varchar(50) null comment '公司id',
	enable int null comment '启用状态',
	create_time timestamp null comment '创建时间',
	update_time timestamp null comment '创建时间',
	admin int null comment '是否管理员'
)
comment '角色';

create table t_role_user
(
	id bigint auto_increment
		primary key,
	role_id bigint not null,
	user_id bigint not null
)
comment '用户角色关联表';

create table t_user
(
	id bigint auto_increment
		primary key,
	username varchar(100) not null comment '用户名',
	password varchar(200) null comment '密码',
	nickname varchar(200) null comment '昵称',
	company_id varchar(100) null comment '公司信息',
	gander int not null comment '性别',
	age int not null,
	mail varchar(100) null comment '邮件',
	phone varchar(30) null comment '电话',
	create_time datetime null,
	update_time datetime null,
	user_desc varchar(200) null comment '用户简介'
)
comment '用户表';

INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('admin', '123456', '管理员', '1', 1, 22, 'default.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户admin用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('root', 'root', '弱鸡管理员', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao3', '123456', '王浩wanghao3', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao4', '123456', '王浩wanghao4', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao5', '123456', '王浩wanghao5', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao6', '123456', '王浩wanghao6', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao7', '123456', '王浩wanghao7', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao8', '123456', '王浩wanghao8', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao9', '123456', '王浩wanghao9', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao10', '123456', '王浩wanghao10', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao11', '123456', '王浩wanghao11', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao12', '123456', '王浩wanghao12', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao13', '123456', '王浩wanghao13', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao14', '123456', '王浩wanghao14', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao15', '123456', '王浩wanghao15', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao16', '123456', '王浩wanghao16', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao17', '123456', '王浩wanghao17', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao18', '123456', '王浩wanghao18', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao19', '123456', '王浩wanghao19', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao20', '123456', '王浩wanghao20', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao21', '123456', '王浩wanghao21', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao22', '123456', '王浩wanghao22', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao23', '123456', '王浩wanghao23', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao24', '123456', '王浩wanghao24', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao25', '123456', '王浩wanghao25', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao26', '123456', '王浩wanghao26', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao27', '123456', '王浩wanghao27', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao28', '123456', '王浩wanghao28', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao29', '123456', '王浩wanghao29', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao30', '123456', '王浩wanghao30', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao31', '123456', '王浩wanghao31', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao32', '123456', '王浩wanghao32', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao33', '123456', '王浩wanghao33', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao34', '123456', '王浩wanghao34', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao35', '123456', '王浩wanghao35', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao36', '123456', '王浩wanghao36', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao37', '123456', '王浩wanghao37', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao38', '123456', '王浩wanghao38', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao39', '123456', '王浩wanghao39', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao40', '123456', '王浩wanghao40', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao41', '123456', '王浩wanghao41', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao42', '123456', '王浩wanghao42', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');
INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time, user_desc) VALUES ('wanghao43', '123456', '王浩wanghao43', '1', 1, 22, 'root.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11', '这里是用户root用户信息');

