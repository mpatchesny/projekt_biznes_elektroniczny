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

/* @PrestaShop/Admin/Module/Includes/modal_read_more_content.html.twig */
class __TwigTemplate_0df248690d2dbd16ae2c582435d21e3166624fbc068637b1bfe5d45f360e54cc extends \Twig\Template
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
        $context["ats"] = $this->getAttribute(($context["module"] ?? null), "attributes", []);
        // line 26
        list($context["name"], $context["displayName"], $context["nbRates"], $context["starsRate"], $context["img"], $context["serviceUrl"], $context["version"], $context["cover"], $context["additionalDescription"], $context["fullDescription"], $context["changeLog"], $context["customerBenefits"], $context["demoVideo"], $context["author"], $context["notFoundImg"], $context["features"], $context["badges"]) =         [$this->getAttribute(        // line 29
($context["ats"] ?? null), "name", []), $this->getAttribute(($context["ats"] ?? null), "displayName", []), $this->getAttribute(($context["ats"] ?? null), "nbRates", []), $this->getAttribute(($context["ats"] ?? null), "starsRate", []), $this->getAttribute(($context["ats"] ?? null), "img", []), ((($this->getAttribute(        // line 30
($context["ats"] ?? null), "serviceUrl", [], "any", true, true) && (twig_length_filter($this->env, $this->getAttribute(($context["ats"] ?? null), "serviceUrl", [])) > 0))) ? ($this->getAttribute(($context["ats"] ?? null), "serviceUrl", [])) : (false)), $this->getAttribute(        // line 31
($context["ats"] ?? null), "version", []), $this->getAttribute(($context["ats"] ?? null), "cover", []), ((($this->getAttribute(        // line 32
($context["ats"] ?? null), "additionalDescription", [], "any", true, true) && (twig_length_filter($this->env, $this->getAttribute(($context["ats"] ?? null), "additionalDescription", [])) > 0))) ? ($this->getAttribute(($context["ats"] ?? null), "additionalDescription", [])) : (false)), ((($this->getAttribute(        // line 33
($context["ats"] ?? null), "fullDescription", [], "any", true, true) && (twig_length_filter($this->env, $this->getAttribute(($context["ats"] ?? null), "fullDescription", [])) > 0))) ? ($this->getAttribute(($context["ats"] ?? null), "fullDescription", [])) : (false)), ((($this->getAttribute(        // line 34
($context["ats"] ?? null), "changeLog", [], "any", true, true) && (twig_length_filter($this->env, $this->getAttribute(($context["ats"] ?? null), "changeLog", [])) > 0))) ? ($this->getAttribute(($context["ats"] ?? null), "changeLog", [])) : (false)), ((($this->getAttribute(        // line 35
($context["ats"] ?? null), "customer_benefits", [], "any", true, true) && (twig_length_filter($this->env, $this->getAttribute(($context["ats"] ?? null), "customer_benefits", [])) > 0))) ? ($this->getAttribute(($context["ats"] ?? null), "customer_benefits", [])) : (false)), ((($this->getAttribute(        // line 36
($context["ats"] ?? null), "demo_video", [], "any", true, true) && (twig_length_filter($this->env, $this->getAttribute(($context["ats"] ?? null), "demo_video", [])) > 0))) ? ($this->getAttribute(($context["ats"] ?? null), "demo_video", [])) : (false)), $this->getAttribute(        // line 37
($context["ats"] ?? null), "author", []), "https://cdn4.iconfinder.com/data/icons/ballicons-2-free/100/box-512.png", $this->getAttribute(        // line 38
($context["ats"] ?? null), "features", []), ((($this->getAttribute(        // line 39
($context["ats"] ?? null), "badges", [], "any", true, true) && (twig_length_filter($this->env, $this->getAttribute(($context["ats"] ?? null), "badges", [])) > 0))) ? ($this->getAttribute(($context["ats"] ?? null), "badges", [])) : (false))];
        // line 41
        echo "<div class=\"modal-dialog module-modal-dialog\">
  <!-- Modal content-->
  <div class=\"modal-content module-modal-content no-padding\">
    <div class=\"modal-header module-modal-header\">
      ";
        // line 45
        if ((($context["nbRates"] ?? null) > 0)) {
            // line 46
            echo "        <div class=\"read-more-stars module-star-ranking-grid-";
            echo twig_escape_filter($this->env, ($context["starsRate"] ?? null), "html", null, true);
            echo "\">
          (
          ";
            // line 48
            echo twig_escape_filter($this->env, ($context["nbRates"] ?? null), "html", null, true);
            echo "
          )
        </div>
      ";
        }
        // line 52
        echo "      <div>
        <img class=\"module-logo-thumb\" height=\"57\" width=\"57\" src=\"";
        // line 53
        echo twig_escape_filter($this->env, ($context["img"] ?? null), "html", null, true);
        echo "\" alt=\"";
        echo twig_escape_filter($this->env, ($context["displayName"] ?? null), "html", null, true);
        echo "\"/>
        <div class=\"modal-title module-modal-title\">
          <h1>";
        // line 55
        echo twig_escape_filter($this->env, ($context["displayName"] ?? null), "html", null, true);
        echo "<br>
            <small class=\"version small-text\">
              ";
        // line 57
        if ((array_key_exists("serviceUrl", $context) && (twig_length_filter($this->env, ($context["serviceUrl"] ?? null)) > 0))) {
            // line 58
            echo "                ";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Service by %author%", ["%author%" => ($context["author"] ?? null)], "Admin.Modules.Feature"), "html", null, true);
            echo "
              ";
        } else {
            // line 60
            echo "                ";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("v%version% by %author%", ["%version%" => ($context["version"] ?? null), "%author%" => ($context["author"] ?? null)], "Admin.Modules.Feature"), "html", null, true);
            echo "
              ";
        }
        // line 62
        echo "            </small>
          </h1>

        </div>
      </div>
      <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-label=\"Close\">
        <span aria-hidden=\"true\">&times;</span>
      </button>
    </div>

    <div class=\"modal-body row module-modal-body\">
      <div class=\"col-md-12 module-big-cover\">
        <img src=\"";
        // line 74
        if ($this->getAttribute(($context["cover"] ?? null), "big", [], "any", true, true)) {
            echo twig_escape_filter($this->env, $this->getAttribute(($context["cover"] ?? null), "big", []), "html", null, true);
        } else {
            echo twig_escape_filter($this->env, ($context["notFoundImg"] ?? null), "html", null, true);
        }
        echo "\"/>
      </div>
      <div class=\"col-md-12 module-menu-readmore\">
        <nav class=\"navbar navbar-light\">
          ";
        // line 79
        echo "          <ul class=\"nav nav-pills\">
            <li class=\"nav-item\">
              <a class=\"nav-link module-readmore-tab active\" data-toggle=\"tab\" href=\"#overview-";
        // line 81
        echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
        echo "\">";
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Overview", [], "Admin.Modules.Feature"), "html", null, true);
        echo "</a>
            </li>
            ";
        // line 83
        if (($context["additionalDescription"] ?? null)) {
            // line 84
            echo "              <li class=\"nav-item\">
                <a class=\"nav-link module-readmore-tab\" data-toggle=\"tab\" href=\"#additional-";
            // line 85
            echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
            echo "\">";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Additional information", [], "Admin.Modules.Feature"), "html", null, true);
            echo "</a>
              </li>
            ";
        }
        // line 88
        echo "            ";
        if (($context["customerBenefits"] ?? null)) {
            // line 89
            echo "              <li class=\"nav-item\">
                <a class=\"nav-link module-readmore-tab\" data-toggle=\"tab\" href=\"#customer_benefits-";
            // line 90
            echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
            echo "\">";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Benefits", [], "Admin.Modules.Feature"), "html", null, true);
            echo "</a>
              </li>
            ";
        }
        // line 93
        echo "            ";
        if (($context["features"] ?? null)) {
            // line 94
            echo "              <li class=\"nav-item\">
                <a class=\"nav-link module-readmore-tab\" data-toggle=\"tab\" href=\"#features-";
            // line 95
            echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
            echo "\">";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Features", [], "Admin.Modules.Feature"), "html", null, true);
            echo "</a>
              </li>
            ";
        }
        // line 98
        echo "            ";
        if (($context["demoVideo"] ?? null)) {
            // line 99
            echo "              <li class=\"nav-item\">
                <a class=\"nav-link module-readmore-tab\" data-toggle=\"tab\" href=\"#demo_video-";
            // line 100
            echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
            echo "\">";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Demo video", [], "Admin.Modules.Feature"), "html", null, true);
            echo "</a>
              </li>
            ";
        }
        // line 103
        echo "            ";
        if (($context["changeLog"] ?? null)) {
            // line 104
            echo "              <li class=\"nav-item\">
                <a class=\"nav-link module-readmore-tab\" data-toggle=\"tab\" href=\"#changelog-";
            // line 105
            echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
            echo "\">";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Changelog", [], "Admin.Modules.Feature"), "html", null, true);
            echo "</a>
              </li>
            ";
        }
        // line 108
        echo "            ";
        // line 109
        echo "          </ul>
        </nav>
        <div class=\"tab-content\">
          ";
        // line 113
        echo "          <div id=\"overview-";
        echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
        echo "\" class=\"tab-pane fade in active show\">
            <p class=\"module-readmore-tab-content\">
              ";
        // line 115
        if (($context["fullDescription"] ?? null)) {
            // line 116
            echo "                ";
            echo ($context["fullDescription"] ?? null);
            echo "
              ";
        } else {
            // line 118
            echo "                ";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("No description found for this module :(", [], "Admin.Modules.Notification"), "html", null, true);
            echo "
              ";
        }
        // line 120
        echo "            </p>
            ";
        // line 121
        if (($this->getAttribute($this->getAttribute(($context["module"] ?? null), "attributes", [], "any", false, true), "multistoreCompatibility", [], "any", true, true) &&  !($this->getAttribute($this->getAttribute(($context["module"] ?? null), "attributes", []), "multistoreCompatibility", []) === twig_constant("\\Module::MULTISTORE_COMPATIBILITY_UNKNOWN")))) {
            // line 122
            echo "              <div class=\"module-readmore-multistore-content\">
                <h3>";
            // line 123
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Multistore compatibility:", [], "Admin.Modules.Feature"), "html", null, true);
            echo "</h3>
                ";
            // line 124
            if (($this->getAttribute($this->getAttribute(($context["module"] ?? null), "attributes", []), "multistoreCompatibility", []) === twig_constant("\\Module::MULTISTORE_COMPATIBILITY_YES"))) {
                // line 125
                echo "                  ";
                echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("This module is compatible with the multistore feature. It can be either:", [], "Admin.Modules.Feature"), "html", null, true);
                echo "
                  <ul>
                    <li>";
                // line 127
                echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("configured differently from one store to another;", [], "Admin.Modules.Feature"), "html", null, true);
                echo "</li>
                    <li>";
                // line 128
                echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("configured quickly in the same way on all stores thanks to the all shops context or to the group of shops;", [], "Admin.Modules.Feature"), "html", null, true);
                echo "</li>
                    <li>";
                // line 129
                echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("or even activated for one store and deactivated for another.", [], "Admin.Modules.Feature"), "html", null, true);
                echo "</li>
                  </ul>
                ";
            } elseif (($this->getAttribute($this->getAttribute(            // line 131
($context["module"] ?? null), "attributes", []), "multistoreCompatibility", []) === twig_constant("\\Module::MULTISTORE_COMPATIBILITY_PARTIAL"))) {
                // line 132
                echo "                  ";
                echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("This module is partially compatible with the multistore feature. Some of its options might not be available.", [], "Admin.Modules.Feature"), "html", null, true);
                echo "
                ";
            } elseif (($this->getAttribute($this->getAttribute(            // line 133
($context["module"] ?? null), "attributes", []), "multistoreCompatibility", []) === twig_constant("\\Module::MULTISTORE_COMPATIBILITY_NOT_CONCERNED"))) {
                // line 134
                echo "                  ";
                echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("This module is not compatible with the multistore feature because it would not be useful.", [], "Admin.Modules.Feature"), "html", null, true);
                echo "
                ";
            } elseif (($this->getAttribute($this->getAttribute(            // line 135
($context["module"] ?? null), "attributes", []), "multistoreCompatibility", []) === twig_constant("\\Module::MULTISTORE_COMPATIBILITY_NO"))) {
                // line 136
                echo "                  ";
                echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("This module is not compatible with the multistore feature. It means that its configuration applies to all stores.", [], "Admin.Modules.Feature"), "html", null, true);
                echo "
                ";
            }
            // line 138
            echo "              </div>
            ";
        }
        // line 140
        echo "          </div>

          <div id=\"additional-";
        // line 142
        echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
        echo "\" class=\"tab-pane fade\">
            <p class=\"module-readmore-tab-content\">
              ";
        // line 144
        if (($context["additionalDescription"] ?? null)) {
            // line 145
            echo "                ";
            echo ($context["additionalDescription"] ?? null);
            echo "
              ";
        } else {
            // line 147
            echo "                ";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("No additional description provided for this module :(", [], "Admin.Modules.Notification"), "html", null, true);
            echo "
              ";
        }
        // line 149
        echo "            </p>
          </div>

          <div id=\"features-";
        // line 152
        echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
        echo "\" class=\"tab-pane fade\">
            <p class=\"module-readmore-tab-content\">
              ";
        // line 154
        if (($context["features"] ?? null)) {
            // line 155
            echo "                ";
            echo ($context["features"] ?? null);
            echo "
              ";
        } else {
            // line 157
            echo "                ";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("No feature list provided for this module :(", [], "Admin.Modules.Notification"), "html", null, true);
            echo "
              ";
        }
        // line 159
        echo "            </p>
          </div>

          <div id=\"customer_benefits-";
        // line 162
        echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
        echo "\" class=\"tab-pane fade\">
            <p class=\"module-readmore-tab-content\">
              ";
        // line 164
        if (($context["customerBenefits"] ?? null)) {
            // line 165
            echo "                ";
            echo ($context["customerBenefits"] ?? null);
            echo "
              ";
        } else {
            // line 167
            echo "                ";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("No customer benefits notes found for this module :(", [], "Admin.Modules.Notification"), "html", null, true);
            echo "
              ";
        }
        // line 169
        echo "            </p>
          </div>

          <div id=\"demo_video-";
        // line 172
        echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
        echo "\" class=\"tab-pane fade\">
            <p class=\"module-readmore-tab-content\">
              ";
        // line 174
        if (($context["demoVideo"] ?? null)) {
            // line 175
            echo "                ";
            echo $this->env->getExtension('PrestaShopBundle\Twig\LayoutExtension')->getYoutubeLink(($context["demoVideo"] ?? null));
            echo "
              ";
        } else {
            // line 177
            echo "                ";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("No demonstration video found for this module :(", [], "Admin.Modules.Notification"), "html", null, true);
            echo "
              ";
        }
        // line 179
        echo "            </p>
          </div>

          <div id=\"changelog-";
        // line 182
        echo twig_escape_filter($this->env, ($context["name"] ?? null), "html", null, true);
        echo "\" class=\"tab-pane fade\">
            ";
        // line 183
        if (($context["changeLog"] ?? null)) {
            // line 184
            echo "              <ul class=\"module-readmore-tab-content\">
                ";
            // line 185
            $context['_parent'] = $context;
            $context['_seq'] = twig_ensure_traversable(twig_reverse_filter($this->env, $this->env->getExtension('PrestaShopBundle\Twig\DataFormatterExtension')->arrayCast(($context["changeLog"] ?? null))));
            foreach ($context['_seq'] as $context["version"] => $context["lines"]) {
                // line 186
                echo "                  <li>
                    <b>";
                // line 187
                echo twig_escape_filter($this->env, $context["version"], "html", null, true);
                echo ":</b>
                    ";
                // line 188
                $context['_parent'] = $context;
                $context['_seq'] = twig_ensure_traversable($context["lines"]);
                foreach ($context['_seq'] as $context["_key"] => $context["line"]) {
                    // line 189
                    echo "                      ";
                    echo twig_escape_filter($this->env, $context["line"], "html", null, true);
                    echo "<br/>
                    ";
                }
                $_parent = $context['_parent'];
                unset($context['_seq'], $context['_iterated'], $context['_key'], $context['line'], $context['_parent'], $context['loop']);
                $context = array_intersect_key($context, $_parent) + $_parent;
                // line 191
                echo "                  </li>
                ";
            }
            $_parent = $context['_parent'];
            unset($context['_seq'], $context['_iterated'], $context['version'], $context['lines'], $context['_parent'], $context['loop']);
            $context = array_intersect_key($context, $_parent) + $_parent;
            // line 193
            echo "              </ul>
            ";
        } else {
            // line 195
            echo "              ";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("No changelog provided for this module :(", [], "Admin.Modules.Notification"), "html", null, true);
            echo "
            ";
        }
        // line 197
        echo "          </div>
          ";
        // line 199
        echo "        </div>
      </div>
    </div>

    <div class=\"modal-footer module-modal-footer\">
      <div class=\"module-stars-price\">
        <div class=\"module-price text-sm-right\">
          ";
        // line 206
        if ((($this->getAttribute($this->getAttribute(($context["module"] ?? null), "attributes", []), "url_active", []) == "buy") && ($this->getAttribute($this->getAttribute($this->getAttribute(($context["module"] ?? null), "attributes", []), "price", []), "raw", []) != "0.00"))) {
            // line 207
            echo "            ";
            echo twig_escape_filter($this->env, $this->getAttribute($this->getAttribute($this->getAttribute(($context["module"] ?? null), "attributes", []), "price", []), "displayPrice", []), "html", null, true);
            echo "
          ";
        } elseif (($this->getAttribute($this->getAttribute(        // line 208
($context["module"] ?? null), "attributes", []), "url_active", []) != "buy")) {
            // line 209
            echo "            ";
            echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Free", [], "Admin.Modules.Feature"), "html", null, true);
            echo "
          ";
        }
        // line 211
        echo "        </div>
      </div>
      <div class=\"module-badges-action\">
        <div class=\"float-left module-badges-display\">
          ";
        // line 215
        $context['_parent'] = $context;
        $context['_seq'] = twig_ensure_traversable(($context["badges"] ?? null));
        foreach ($context['_seq'] as $context["_key"] => $context["badge"]) {
            // line 216
            echo "            <img src=\"";
            echo twig_escape_filter($this->env, $this->getAttribute($context["badge"], "img", []), "html", null, true);
            echo "\" alt=\"";
            echo twig_escape_filter($this->env, $this->getAttribute($context["badge"], "label", []), "html", null, true);
            echo "\"/>
            ";
            // line 217
            echo twig_escape_filter($this->env, $this->getAttribute($context["badge"], "label", []), "html", null, true);
            echo "
          ";
        }
        $_parent = $context['_parent'];
        unset($context['_seq'], $context['_iterated'], $context['_key'], $context['badge'], $context['_parent'], $context['loop']);
        $context = array_intersect_key($context, $_parent) + $_parent;
        // line 219
        echo "        </div>
        <div class=\"float-right module-action\">
          ";
        // line 221
        $this->loadTemplate("@PrestaShop/Admin/Module/Includes/action_menu.html.twig", "@PrestaShop/Admin/Module/Includes/modal_read_more_content.html.twig", 221)->display(twig_array_merge($context, ["module" => ($context["module"] ?? null), "level" => ($context["level"] ?? null)]));
        // line 222
        echo "        </div>
      </div>
    </div>
  </div>
</div>
";
    }

    public function getTemplateName()
    {
        return "@PrestaShop/Admin/Module/Includes/modal_read_more_content.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  494 => 222,  492 => 221,  488 => 219,  480 => 217,  473 => 216,  469 => 215,  463 => 211,  457 => 209,  455 => 208,  450 => 207,  448 => 206,  439 => 199,  436 => 197,  430 => 195,  426 => 193,  419 => 191,  410 => 189,  406 => 188,  402 => 187,  399 => 186,  395 => 185,  392 => 184,  390 => 183,  386 => 182,  381 => 179,  375 => 177,  369 => 175,  367 => 174,  362 => 172,  357 => 169,  351 => 167,  345 => 165,  343 => 164,  338 => 162,  333 => 159,  327 => 157,  321 => 155,  319 => 154,  314 => 152,  309 => 149,  303 => 147,  297 => 145,  295 => 144,  290 => 142,  286 => 140,  282 => 138,  276 => 136,  274 => 135,  269 => 134,  267 => 133,  262 => 132,  260 => 131,  255 => 129,  251 => 128,  247 => 127,  241 => 125,  239 => 124,  235 => 123,  232 => 122,  230 => 121,  227 => 120,  221 => 118,  215 => 116,  213 => 115,  207 => 113,  202 => 109,  200 => 108,  192 => 105,  189 => 104,  186 => 103,  178 => 100,  175 => 99,  172 => 98,  164 => 95,  161 => 94,  158 => 93,  150 => 90,  147 => 89,  144 => 88,  136 => 85,  133 => 84,  131 => 83,  124 => 81,  120 => 79,  109 => 74,  95 => 62,  89 => 60,  83 => 58,  81 => 57,  76 => 55,  69 => 53,  66 => 52,  59 => 48,  53 => 46,  51 => 45,  45 => 41,  43 => 39,  42 => 38,  41 => 37,  40 => 36,  39 => 35,  38 => 34,  37 => 33,  36 => 32,  35 => 31,  34 => 30,  33 => 29,  32 => 26,  30 => 25,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Source("", "@PrestaShop/Admin/Module/Includes/modal_read_more_content.html.twig", "/var/www/html/src/PrestaShopBundle/Resources/views/Admin/Module/Includes/modal_read_more_content.html.twig");
    }
}
