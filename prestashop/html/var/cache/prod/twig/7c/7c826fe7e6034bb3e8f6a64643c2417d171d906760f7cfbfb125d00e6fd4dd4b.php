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

/* @PrestaShop/Admin/Configure/AdvancedParameters/Backup/Blocks/download_file.html.twig */
class __TwigTemplate_32d3d50349fdb2c18e8a28d7b272214f022eff3e390f49af5c20a9a793b78538 extends \Twig\Template
{
    public function __construct(Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = [
        ];
    }

    protected function doDisplay(array $context, array $blocks = [])
    {
        // line 25
        echo "
";
        // line 27
        echo "
<div class=\"card\">
  <h3 class=\"card-header\">
    <i class=\"material-icons\">cloud_download</i>
    ";
        // line 31
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Download", [], "Admin.Actions"), "html", null, true);
        echo "
  </h3>
  <div class=\"card-body\">
    <p>
      <a href=\"";
        // line 35
        echo twig_escape_filter($this->env, $this->getAttribute(($context["downloadFile"] ?? null), "url", []), "html", null, true);
        echo "\" class=\"btn btn-outline-primary\">
        <i class=\"material-icons\">cloud_download</i>
        ";
        // line 37
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Download the backup file (%s MB)", ["%s" => $this->getAttribute(($context["downloadFile"] ?? null), "size", [])], "Admin.Advparameters.Feature"), "html", null, true);
        echo "
      </a>
    </p>
    <p>";
        // line 40
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Tip: You can also download this file from your FTP server. Backup files are located in the \"/adminXXXX/backups\" directory.", [], "Admin.Advparameters.Feature"), "html", null, true);
        echo "</p>
  </div>
</div>
";
    }

    public function getTemplateName()
    {
        return "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/Blocks/download_file.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  57 => 40,  51 => 37,  46 => 35,  39 => 31,  33 => 27,  30 => 25,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Source("", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/Blocks/download_file.html.twig", "/var/www/html/src/PrestaShopBundle/Resources/views/Admin/Configure/AdvancedParameters/Backup/Blocks/download_file.html.twig");
    }
}
