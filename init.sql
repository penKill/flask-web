-- auto-generated definition
create table t_user
(
    id          bigint auto_increment
        primary key,
    username    varchar(100) not null comment '用户名',
    password    varchar(200) null comment '密码',
    nickname    varchar(200) null comment '昵称',
    company_id  varchar(100) null comment '公司信息',
    gander      int          not null comment '性别',
    age         int          not null,
    mail        varchar(100) null comment '邮件',
    phone       varchar(30)  null comment '电话',
    create_time datetime     null,
    update_time datetime     null
)
    comment '用户表';

INSERT INTO t_user (username, password, nickname, company_id, gander, age, mail, phone, create_time, update_time) VALUES ('admin', '123456', '管理员', '1', 1, 22, 'default.mail@imail.com', '18380387621', '2022-01-04 11:03:11', '2022-01-04 11:03:11');