<?php

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.

if (\class_exists(\ContainerPt74eu9\appProdProjectContainer::class, false)) {
    // no-op
} elseif (!include __DIR__.'/ContainerPt74eu9/appProdProjectContainer.php') {
    touch(__DIR__.'/ContainerPt74eu9.legacy');

    return;
}

if (!\class_exists(appProdProjectContainer::class, false)) {
    \class_alias(\ContainerPt74eu9\appProdProjectContainer::class, appProdProjectContainer::class, false);
}

return new \ContainerPt74eu9\appProdProjectContainer([
    'container.build_hash' => 'Pt74eu9',
    'container.build_id' => '0289137e',
    'container.build_time' => 1697738345,
], __DIR__.\DIRECTORY_SEPARATOR.'ContainerPt74eu9');
