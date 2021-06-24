<?php
function adminer_object() {
    class AdminerSoftware extends Adminer {
        function name() {
            return 'SKY EYE';
        }
        function credentials() {
            return array('10.10.10.2', 'root', 'adminermysql');
        }
        function database() {
            return 'sky_eye';
        }
    }
    return new AdminerSoftware;
}
include './editor.php';
