<?php
/* Smarty version 3.1.43, created on 2022-12-09 22:18:05
  from '/var/www/html/themes/classic/templates/catalog/_partials/product-additional-info.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.43',
  'unifunc' => 'content_6393a60d6b18f6_62227517',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'e917709f9a6d5bc9cd7854e1367f385d8ec4c0e8' => 
    array (
      0 => '/var/www/html/themes/classic/templates/catalog/_partials/product-additional-info.tpl',
      1 => 1658334665,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6393a60d6b18f6_62227517 (Smarty_Internal_Template $_smarty_tpl) {
?><div class="product-additional-info js-product-additional-info">
  <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['hook'][0], array( array('h'=>'displayProductAdditionalInfo','product'=>$_smarty_tpl->tpl_vars['product']->value),$_smarty_tpl ) );?>

</div>
<?php }
}
