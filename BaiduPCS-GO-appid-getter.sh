#!/bin/bash

item=266718
function check(){
    BaiduPCS-Go config set -appid=$item &> /dev/null
    BaiduPCS-Go ls | grep -q 遇到错误
    if [ $? != 0 ];then
        echo "当前可用appid：$item ，已设置成功，BaiduPCS-Go 现可用正常使用了！"
    else
        let item+=1
        check
    fi
}
check
