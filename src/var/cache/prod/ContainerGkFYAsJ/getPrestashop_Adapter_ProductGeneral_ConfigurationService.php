<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;
use Symfony\Component\DependencyInjection\Exception\RuntimeException;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'prestashop.adapter.product_general.configuration' shared service.

return $this->services['prestashop.adapter.product_general.configuration'] = new \PrestaShop\PrestaShop\Adapter\Product\GeneralConfiguration(($this->services['PrestaShop\\PrestaShop\\Adapter\\Configuration'] ?? ($this->services['PrestaShop\\PrestaShop\\Adapter\\Configuration'] = new \PrestaShop\PrestaShop\Adapter\Configuration())), ($this->services['PrestaShop\\PrestaShop\\Adapter\\Product\\SpecificPrice\\Update\\SpecificPricePriorityUpdater'] ?? $this->load('getSpecificPricePriorityUpdaterService.php')));
