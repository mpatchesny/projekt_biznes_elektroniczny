<?php
/* Smarty version 3.1.43, created on 2022-11-17 19:22:52
  from '/var/www/html/admin123/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.43',
  'unifunc' => 'content_63767bfc63c6c9_53843417',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '64688e68ee930bff99e70c3491eb0ce342aed178' => 
    array (
      0 => '/var/www/html/admin123/themes/default/template/content.tpl',
      1 => 1658334665,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_63767bfc63c6c9_53843417 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>

<div class="row">
	<div class="col-lg-12">
		<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
