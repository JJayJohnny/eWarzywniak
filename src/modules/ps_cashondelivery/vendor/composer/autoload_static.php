<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInitdac3f7f7c2290d4c42066b57a3e3c014
{
    public static $classMap = array (
        'Ps_Cashondelivery' => __DIR__ . '/../..' . '/ps_cashondelivery.php',
        'Ps_CashondeliveryValidationModuleFrontController' => __DIR__ . '/../..' . '/controllers/front/validation.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->classMap = ComposerStaticInitdac3f7f7c2290d4c42066b57a3e3c014::$classMap;

        }, null, ClassLoader::class);
    }
}
