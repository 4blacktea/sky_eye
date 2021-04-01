<?php
function adminer_object() {
    class AdminerSoftware extends Adminer {
        function name() {
            // custom name in title and heading
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
