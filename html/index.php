<?php
function adminer_object() {
    class AdminerSoftware extends Adminer {
        function name() {
            return 'SKY EYE';
        }
        function credentials() {
            return array('10.122.104.158', 'vuluser', 'VulPassword4!');
        }
        function database() {
            return 'vuldb_v2';
        }
    }
    return new AdminerSoftware;
}
include './editor.php';
