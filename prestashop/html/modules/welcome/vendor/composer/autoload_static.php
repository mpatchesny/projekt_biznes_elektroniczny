<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit3f7c14459a5367047075af9ae9ef85b7
{
    public static $prefixLengthsPsr4 = array (
        'O' => 
        array (
            'OnBoarding\\' => 11,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'OnBoarding\\' => 
        array (
            0 => __DIR__ . '/../..' . '/OnBoarding',
        ),
    );

    public static $classMap = array (
        'OnBoarding\\Configuration' => __DIR__ . '/../..' . '/OnBoarding/Configuration.php',
        'OnBoarding\\OnBoarding' => __DIR__ . '/../..' . '/OnBoarding/OnBoarding.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit3f7c14459a5367047075af9ae9ef85b7::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit3f7c14459a5367047075af9ae9ef85b7::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInit3f7c14459a5367047075af9ae9ef85b7::$classMap;

        }, null, ClassLoader::class);
    }
}
