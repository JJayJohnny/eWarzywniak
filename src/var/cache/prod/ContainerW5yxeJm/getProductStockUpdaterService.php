<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;
use Symfony\Component\DependencyInjection\Exception\RuntimeException;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the private 'PrestaShop\PrestaShop\Adapter\Product\Stock\Update\ProductStockUpdater' shared autowired service.

return $this->privates['PrestaShop\\PrestaShop\\Adapter\\Product\\Stock\\Update\\ProductStockUpdater'] = new \PrestaShop\PrestaShop\Adapter\Product\Stock\Update\ProductStockUpdater(($this->privates['PrestaShop\\PrestaShop\\Core\\Stock\\StockManager'] ?? ($this->privates['PrestaShop\\PrestaShop\\Core\\Stock\\StockManager'] = new \PrestaShop\PrestaShop\Core\Stock\StockManager())), ($this->services['PrestaShop\\PrestaShop\\Adapter\\Product\\Repository\\ProductRepository'] ?? $this->load('getProductRepositoryService.php')), ($this->privates['PrestaShop\\PrestaShop\\Adapter\\Product\\Stock\\Repository\\StockAvailableRepository'] ?? $this->load('getStockAvailableRepositoryService.php')), ($this->services['PrestaShop\\PrestaShop\\Adapter\\Product\\Stock\\Repository\\MovementReasonRepository'] ?? $this->load('getMovementReasonRepositoryService.php')), ($this->services['PrestaShop\\PrestaShop\\Adapter\\Configuration'] ?? ($this->services['PrestaShop\\PrestaShop\\Adapter\\Configuration'] = new \PrestaShop\PrestaShop\Adapter\Configuration())), ($this->services['PrestaShop\\PrestaShop\\Adapter\\HookManager'] ?? ($this->services['PrestaShop\\PrestaShop\\Adapter\\HookManager'] = new \PrestaShop\PrestaShop\Adapter\HookManager())));
