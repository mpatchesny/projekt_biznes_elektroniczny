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

/* @Modules/ps_metrics/views/templates/admin/error.html.twig */
class __TwigTemplate_67980bda1c3fa1f2c94206f3bd87958a899255626f765f321c6dd67dd299d571 extends \Twig\Template
{
    public function __construct(Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = [
            'content' => [$this, 'block_content'],
            'stylesheets' => [$this, 'block_stylesheets'],
            'javascripts' => [$this, 'block_javascripts'],
        ];
    }

    protected function doDisplay(array $context, array $blocks = [])
    {
        // line 19
        echo " 
 ";
        // line 20
        $this->displayBlock('content', $context, $blocks);
        // line 29
        echo "
";
        // line 30
        $this->displayBlock('stylesheets', $context, $blocks);
        // line 80
        echo "
";
        // line 81
        $this->displayBlock('javascripts', $context, $blocks);
    }

    // line 20
    public function block_content($context, array $blocks = [])
    {
        // line 21
        echo "    <div id=\"error-loading-app-content\">
        <div id=\"error-loading-app-content-icon\"> ! </div>
        <h2> Oops, an error occured... </h2>
        <p> We are currently unable to display your KPI's. </p>
        <p> Please make sure you are using the latest version of PrestaShop Metrics. </p>
        <p> If the problem persist, please contact our support team: <b><a href=\"mailto:support-ps-metrics@prestashop.com\" target=\"_blank\">support-ps-metrics@prestashop.com</a></b>.</p>
    </div>
";
    }

    // line 30
    public function block_stylesheets($context, array $blocks = [])
    {
        // line 31
        echo "    <style>
        #error-loading-app {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        #error-loading-app-content{
            margin: 200px auto;
            display: flex;
            flex-direction: column;
            background-color: #FAFAFB;
            border-radius: 5px;
            padding: 50px;
            border: 2px solid #C8D7E4;
            text-align: center;
        }
        #error-loading-app-content-icon{
            font-size: 30px;
            text-align: center;
            color: #FFFFFF;
            background-color: #DADADA;
            border-radius: 50%;
            height: 45px;
            width: 45px;
            margin: auto;
            line-height: 1.4em;

        }
        #error-loading-app-content h2{
            margin: 10px 20px 20px;
            font-weight: bold;
            font-size: 20px;
            line-height: 30px;
        }
        #error-loading-app-content p{
            margin-bottom: 5px;
            font-size: 14px;
            line-height: 20px;
        }

        .hide {
            display: none !important;
        }

        .show {
            display: block;
        }
    </style>
";
    }

    // line 81
    public function block_javascripts($context, array $blocks = [])
    {
        // line 82
        echo "    <script>
        (() => {
            let appIsLoaded = false;
            let currentRecursion = 0;
            let maxRecursion = 150;

            const checkAppIsloaded = () => {
                currentRecursion++;

                if (currentRecursion === maxRecursion) {
                // show error block and hide metrics
                document.getElementById('error-loading-app').classList.add('show');
                document.getElementById('error-loading-app').classList.remove('hide');

                document.getElementById('metrics-app').classList.add('hide');
                document.getElementById('metrics-app').classList.remove('show');
                return;
                }

                if (typeof(window.appIsLoaded) === 'undefined') {
                setTimeout(() => {
                    checkAppIsloaded();
                }, 100);
                }
            }

            checkAppIsloaded();
        })();
    </script>
";
    }

    public function getTemplateName()
    {
        return "@Modules/ps_metrics/views/templates/admin/error.html.twig";
    }

    public function getDebugInfo()
    {
        return array (  122 => 82,  119 => 81,  67 => 31,  64 => 30,  53 => 21,  50 => 20,  46 => 81,  43 => 80,  41 => 30,  38 => 29,  36 => 20,  33 => 19,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Source("", "@Modules/ps_metrics/views/templates/admin/error.html.twig", "/var/www/html/modules/ps_metrics/views/templates/admin/error.html.twig");
    }
}
