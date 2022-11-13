<?php

use Twig\Environment;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Markup;
use Twig\Sandbox\SecurityError;
use Twig\Sandbox\SecurityNotAllowedTagError;
use Twig\Sandbox\SecurityNotAllowedFilterError;
use Twig\Sandbox\SecurityNotAllowedFunctionError;
use Twig\Source;
use Twig\Template;

/* @PrestaShop/Admin/Configure/AdvancedParameters/Backup/index.html.twig */
class __TwigTemplate_dcc5088fa50e81a87fabc86f055eee48ba05a5722152624f0701389f87658e6c extends \Twig\Template
{
    public function __construct(Environment $env)
    {
        parent::__construct($env);

        $this->blocks = [
            'content' => [$this, 'block_content'],
            'backup_download_file' => [$this, 'block_backup_download_file'],
            'backup_alerts' => [$this, 'block_backup_alerts'],
            'backup_listing' => [$this, 'block_backup_listing'],
            'backup_options' => [$this, 'block_backup_options'],
            'javascripts' => [$this, 'block_javascripts'],
        ];
    }

    protected function doGetParent(array $context)
    {
        // line 25
        return "@PrestaShop/Admin/layout.html.twig";
    }

    protected function doDisplay(array $context, array $blocks = [])
    {
        $this->parent = $this->loadTemplate("@PrestaShop/Admin/layout.html.twig", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/index.html.twig", 25);
        $this->parent->display($context, array_merge($this->blocks, $blocks));
    }

    // line 29
    public function block_content($context, array $blocks = [])
    {
        // line 30
        echo "  ";
        $this->displayBlock('backup_download_file', $context, $blocks);
        // line 35
        echo "
  ";
        // line 36
        $this->displayBlock('backup_alerts', $context, $blocks);
        // line 50
        echo "
  ";
        // line 51
        $this->displayBlock('backup_listing', $context, $blocks);
        // line 58
        echo "
  ";
        // line 59
        $this->displayBlock('backup_options', $context, $blocks);
    }

    // line 30
    public function block_backup_download_file($context, array $blocks = [])
    {
        // line 31
        echo "    ";
        if (($context["hasDownloadFile"] ?? null)) {
            // line 32
            echo "      ";
            $this->loadTemplate("@PrestaShop/Admin/Configure/AdvancedParameters/Backup/Blocks/download_file.html.twig", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/index.html.twig", 32)->display($context);
            // line 33
            echo "    ";
        }
        // line 34
        echo "  ";
    }

    // line 36
    public function block_backup_alerts($context, array $blocks = [])
    {
        // line 37
        echo "    ";
        if (($context["multistoreIsUsed"] ?? null)) {
            echo twig_escape_filter($this->env, $this->getAttribute(($context["ps"] ?? null), "infotip", [0 => ($context["multistoreInfoTip"] ?? null), 1 => true], "method"), "html", null, true);
        }
        // line 38
        echo "    <div class=\"row\">
      <div class=\"col\">
        ";
        // line 40
        $this->loadTemplate("@PrestaShop/Admin/Configure/AdvancedParameters/Backup/Blocks/backup_warning.html.twig", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/index.html.twig", 40)->display($context);
        // line 41
        echo "      </div>
    </div>

    <div class=\"row\">
      <div class=\"col\">
        ";
        // line 46
        $this->loadTemplate("@PrestaShop/Admin/Configure/AdvancedParameters/Backup/Blocks/backup_info.html.twig", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/index.html.twig", 46)->display($context);
        // line 47
        echo "      </div>
    </div>
  ";
    }

    // line 51
    public function block_backup_listing($context, array $blocks = [])
    {
        // line 52
        echo "    <div class=\"row\">
      <div class=\"col\">
        ";
        // line 54
        $this->loadTemplate("@PrestaShop/Admin/Common/Grid/grid_panel.html.twig", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/index.html.twig", 54)->display(twig_array_merge($context, ["grid" => ($context["backupGrid"] ?? null)]));
        // line 55
        echo "      </div>
    </div>
  ";
    }

    // line 59
    public function block_backup_options($context, array $blocks = [])
    {
        // line 60
        echo "    <div class=\"row\">
      <div class=\"col\">
        ";
        // line 62
        $this->loadTemplate("@PrestaShop/Admin/Configure/AdvancedParameters/Backup/Blocks/options.html.twig", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/index.html.twig", 62)->display($context);
        // line 63
        echo "      </div>
    </div>
  ";
    }

    // line 68
    public function block_javascripts($context, array $blocks = [])
    {
        // line 69
        echo "    ";
        $this->displayParentBlock("javascripts", $context, $blocks);
        echo "

  <script src=\"";
        // line 71
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\AssetExtension')->getAssetUrl("themes/default/js/bundle/pagination.js"), "html", null, true);
        echo "\"></script>
  <script src=\"";
        // line 72
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\AssetExtension')->getAssetUrl("themes/new-theme/public/backup.bundle.js"), "html", null, true);
        echo "\"></script>
";
    }

    public function getTemplateName()
    {
        return "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/index.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  155 => 72,  151 => 71,  145 => 69,  142 => 68,  136 => 63,  134 => 62,  130 => 60,  127 => 59,  121 => 55,  119 => 54,  115 => 52,  112 => 51,  106 => 47,  104 => 46,  97 => 41,  95 => 40,  91 => 38,  86 => 37,  83 => 36,  79 => 34,  76 => 33,  73 => 32,  70 => 31,  67 => 30,  63 => 59,  60 => 58,  58 => 51,  55 => 50,  53 => 36,  50 => 35,  47 => 30,  44 => 29,  34 => 25,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Source("", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/index.html.twig", "/var/www/html/src/PrestaShopBundle/Resources/views/Admin/Configure/AdvancedParameters/Backup/index.html.twig");
    }
}
