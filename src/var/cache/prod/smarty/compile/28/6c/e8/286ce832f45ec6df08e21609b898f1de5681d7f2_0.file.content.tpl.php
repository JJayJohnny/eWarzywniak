<?php
/* Smarty version 4.3.1, created on 2023-10-11 23:19:44
  from '/var/www/html/admin2137/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '4.3.1',
  'unifunc' => 'content_652711702013d0_20268114',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '286ce832f45ec6df08e21609b898f1de5681d7f2' => 
    array (
      0 => '/var/www/html/admin2137/themes/new-theme/template/content.tpl',
      1 => 1695892354,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_652711702013d0_20268114 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>
<div id="content-message-box"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
