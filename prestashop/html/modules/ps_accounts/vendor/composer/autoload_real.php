<?php

// autoload_real.php @generated by Composer

class ComposerAutoloaderInitc3ee5a9ef31d4a566dfddf2bcceb7086
{
    private static $loader;

    public static function loadClassLoader($class)
    {
        if ('Composer\Autoload\ClassLoader' === $class) {
            require __DIR__ . '/ClassLoader.php';
        }
    }

    /**
     * @return \Composer\Autoload\ClassLoader
     */
    public static function getLoader()
    {
        if (null !== self::$loader) {
            return self::$loader;
        }

        require __DIR__ . '/platform_check.php';

        spl_autoload_register(array('ComposerAutoloaderInitc3ee5a9ef31d4a566dfddf2bcceb7086', 'loadClassLoader'), true, false);
        self::$loader = $loader = new \Composer\Autoload\ClassLoader(\dirname(__DIR__));
        spl_autoload_unregister(array('ComposerAutoloaderInitc3ee5a9ef31d4a566dfddf2bcceb7086', 'loadClassLoader'));

        require __DIR__ . '/autoload_static.php';
        call_user_func(\Composer\Autoload\ComposerStaticInitc3ee5a9ef31d4a566dfddf2bcceb7086::getInitializer($loader));

        $loader->register(false);

        $includeFiles = \Composer\Autoload\ComposerStaticInitc3ee5a9ef31d4a566dfddf2bcceb7086::$files;
        foreach ($includeFiles as $fileIdentifier => $file) {
            composerRequirec3ee5a9ef31d4a566dfddf2bcceb7086($fileIdentifier, $file);
        }

        return $loader;
    }
}

/**
 * @param string $fileIdentifier
 * @param string $file
 * @return void
 */
function composerRequirec3ee5a9ef31d4a566dfddf2bcceb7086($fileIdentifier, $file)
{
    if (empty($GLOBALS['__composer_autoload_files'][$fileIdentifier])) {
        $GLOBALS['__composer_autoload_files'][$fileIdentifier] = true;

        require $file;
    }
}
