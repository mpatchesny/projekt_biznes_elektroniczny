<?php

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.

if (\class_exists(\ContainerSbhpggt\appProdProjectContainer::class, false)) {
    // no-op
} elseif (!include __DIR__.'/ContainerSbhpggt/appProdProjectContainer.php') {
    touch(__DIR__.'/ContainerSbhpggt.legacy');

    return;
}

if (!\class_exists(appProdProjectContainer::class, false)) {
    \class_alias(\ContainerSbhpggt\appProdProjectContainer::class, appProdProjectContainer::class, false);
}

return new \ContainerSbhpggt\appProdProjectContainer([
    'container.build_hash' => 'Sbhpggt',
    'container.build_id' => '6ec0d937',
    'container.build_time' => 1667133336,
], __DIR__.\DIRECTORY_SEPARATOR.'ContainerSbhpggt');
