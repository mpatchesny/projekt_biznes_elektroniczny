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

/* @Modules/ps_metrics/views/templates/admin/metrics.html.twig */
class __TwigTemplate_6995abd189e7f30c737040026b0631b0dd5be69064389df74880e546290de5a8 extends \Twig\Template
{
    public function __construct(Environment $env)
    {
        parent::__construct($env);

        $this->blocks = [
            'content' => [$this, 'block_content'],
            'stylesheets' => [$this, 'block_stylesheets'],
            'javascripts' => [$this, 'block_javascripts'],
        ];
    }

    protected function doGetParent(array $context)
    {
        // line 20
        return $this->loadTemplate(((($context["fullscreen"] ?? null)) ? ("@Modules/ps_metrics/views/templates/admin/fullscreen.html.twig") : ("@PrestaShop/Admin/layout.html.twig")), "@Modules/ps_metrics/views/templates/admin/metrics.html.twig", 20);
    }

    protected function doDisplay(array $context, array $blocks = [])
    {
        $this->getParent($context)->display($context, array_merge($this->blocks, $blocks));
    }

    // line 22
    public function block_content($context, array $blocks = [])
    {
        // line 23
        echo "  <div id=\"error-loading-app\" class=\"hide\">
    ";
        // line 24
        $this->loadTemplate("@Modules/ps_metrics/views/templates/admin/error.html.twig", "@Modules/ps_metrics/views/templates/admin/metrics.html.twig", 24)->display($context);
        // line 25
        echo "  </div>
  <div id=\"metrics-app\"></div>
";
    }

    // line 29
    public function block_stylesheets($context, array $blocks = [])
    {
        // line 30
        echo "  <link rel=\"stylesheet\" href=\"";
        echo twig_escape_filter($this->env, ($context["pathMetricsAssets"] ?? null), "html", null, true);
        echo "\" type=\"text/css\" media=\"all\">

  <style>
    /** Hide native multistore module activation panel, because of visual regressions on non-bootstrap content */
    #content.nobootstrap div.bootstrap.panel {
      display: none;
    }
  </style>

  ";
        // line 39
        if (($context["fullscreen"] ?? null)) {
            // line 40
            echo "  <style>
    body {
      background: #eaebec;
      padding: 20px;
    }
  </style>
  ";
        }
    }

    // line 49
    public function block_javascripts($context, array $blocks = [])
    {
        // line 50
        echo "  <script>
    var oAuthGoogleErrorMessage = '";
        // line 51
        echo ($context["oAuthGoogleErrorMessage"] ?? null);
        echo "';
    var fullscreen = ";
        // line 52
        if (($context["fullscreen"] ?? null)) {
            echo " true ";
        } else {
            echo " false ";
        }
        echo ";
    var contextPsAccounts = ";
        // line 53
        echo twig_jsonencode_filter(($context["contextPsAccounts"] ?? null));
        echo ";
    var metricsApiUrl = '";
        // line 54
        echo ($context["metricsApiUrl"] ?? null);
        echo "';
    var metricsModule = ";
        // line 55
        echo twig_jsonencode_filter(($context["metricsModule"] ?? null));
        echo ";
    var eventBusModule = ";
        // line 56
        echo twig_jsonencode_filter(($context["eventBusModule"] ?? null));
        echo ";
    var accountsModule = ";
        // line 57
        echo twig_jsonencode_filter(($context["accountsModule"] ?? null));
        echo ";
    var graphqlEndpoint = '";
        // line 58
        echo ($context["graphqlEndpoint"] ?? null);
        echo "';
    var isoCode = '";
        // line 59
        echo ($context["isoCode"] ?? null);
        echo "';
    var currencyIsoCode = '";
        // line 60
        echo ($context["currencyIsoCode"] ?? null);
        echo "';
    var currentPage = '";
        // line 61
        echo ($context["currentPage"] ?? null);
        echo "';
    var adminToken = '";
        // line 62
        echo ($context["adminToken"] ?? null);
        echo "';
  </script>

  <script type=\"module\" src=\"";
        // line 65
        echo twig_escape_filter($this->env, ($context["pathMetricsApp"] ?? null), "html", null, true);
        echo "\" async defer></script>

  ";
        // line 67
        if ( !(null === ($context["pathMetricsAppSourceMap"] ?? null))) {
            // line 68
            echo "    <script type=\"application/json\" src=\"";
            echo twig_escape_filter($this->env, ($context["pathMetricsAppSourceMap"] ?? null), "html", null, true);
            echo "\" async defer></script>
  ";
        }
    }

    public function getTemplateName()
    {
        return "@Modules/ps_metrics/views/templates/admin/metrics.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  150 => 68,  148 => 67,  143 => 65,  137 => 62,  133 => 61,  129 => 60,  125 => 59,  121 => 58,  117 => 57,  113 => 56,  109 => 55,  105 => 54,  101 => 53,  93 => 52,  89 => 51,  86 => 50,  83 => 49,  72 => 40,  70 => 39,  57 => 30,  54 => 29,  48 => 25,  46 => 24,  43 => 23,  40 => 22,  31 => 20,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Source("", "@Modules/ps_metrics/views/templates/admin/metrics.html.twig", "/var/www/html/modules/ps_metrics/views/templates/admin/metrics.html.twig");
    }
}
