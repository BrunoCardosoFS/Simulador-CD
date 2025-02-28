from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot, Qt
from PySide6.QtSvgWidgets import QSvgWidget


svg_Page2 = """
<svg width="1000" height="1000" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">
    <rect style="fill:#fff;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" width="1000" height="1000" ry="0"/>
    <path style="fill:#edcf99;fill-opacity:1;stroke-width:1.16646;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M375.225 335.18h249.549v329.64H375.225z"/>
    <path style="fill:#f4f5ed;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M0 0h1000L624.775 335.18h-249.55Z"/>
    <path style="fill:#f3deb9;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M1000 1000V0L624.775 335.18v329.64z"/>
    <path style="fill:#c2a676;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m0 1000 375.225-335.18V335.18L0 0Z"/>
    <path style="fill:#d27857;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m0 1000 375.225-335.18h249.55L1000 1000Z"/>
    <path style="fill:#ffc113;fill-opacity:1;stroke-width:.69453;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M408.928 199.772S434.16 263.827 500 263.827s91.072-64.055 91.072-64.055z"/>
    <path style="fill:#ffa604;fill-opacity:1;stroke-width:1.74962;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M496.915 122.13h6.17v77.642h-6.17z"/>
    <path style="fill:#d68a00;fill-opacity:1;stroke-width:.824063;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M447.235 199.772S443.29 185.634 500 185.634s52.765 14.138 52.765 14.138z"/>
    <path style="fill:#d68a00;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M476.126 115.455h47.748v6.674h-47.748z"/>
    <path style="fill:#a9edf3;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m194.764 686.507 119.204-106.411.458-244.045L194.764 229.16Z"/>
    <path style="fill:#edcf99;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m314.426 336.051-.458 244.045-8.897 7.942V327.695z"/>
    <path style="fill:#f3deb9;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M194.764 229.16 314.426 336.05l-9.355 2.636-110.307-86.539zM194.764 686.507l119.204-106.411-8.897-4.35-110.307 93.3z"/>
    <path style="fill:#fff;fill-opacity:1;stroke-width:.689446;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M643.386 520.073v24.877l10.258 9.172v-43.221z"/>
    <path style="fill:#e3e3e3;fill-opacity:1;stroke-width:2.12474;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M113.078 540.07V444.72l-70.34-62.892v221.135z"/>
    <path style="fill:#fff;fill-opacity:1;stroke-width:1.5603;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M919.014 504.361v56.301l23.216 20.757v-97.815z"/>
    <path style="fill:#a83837;fill-opacity:1;stroke-width:1.16646;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M428.621 379.847H571.38V664.82H428.621z"/>
</svg>
"""

svg_Page3 = """
<svg width="1000" height="1000" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="e">
            <stop style="stop-color:#570b0b;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#380000;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="d">
            <stop style="stop-color:#43a0ff;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#2391ff;stop-opacity:1" offset=".347"/>
            <stop style="stop-color:#0080ff;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="c">
            <stop style="stop-color:#ac5229;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#4f2413;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="b">
            <stop style="stop-color:#f97a1e;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#cc4c05;stop-opacity:1" offset=".512"/>
            <stop style="stop-color:#9d3f0d;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient id="a">
            <stop style="stop-color:#ef762f;stop-opacity:1" offset="0"/>
            <stop style="stop-color:#bf4105;stop-opacity:1" offset=".497"/>
            <stop style="stop-color:#a64109;stop-opacity:1" offset="1"/>
        </linearGradient>
        <linearGradient xlink:href="#a" id="i" x1="0" y1="129.242" x2="1000" y2="129.242" gradientUnits="userSpaceOnUse" gradientTransform="matrix(.90234 0 0 1 48.832 0)"/>
        <linearGradient xlink:href="#b" id="j" x1="0" y1="65.347" x2="1000" y2="65.347" gradientUnits="userSpaceOnUse"/>
        <linearGradient xlink:href="#b" id="k" x1="157.29" y1="732.615" x2="842.71" y2="732.615" gradientUnits="userSpaceOnUse"/>
        <linearGradient xlink:href="#c" id="l" x1="0" y1="971.495" x2="1000" y2="971.495" gradientUnits="userSpaceOnUse"/>
        <linearGradient xlink:href="#d" id="f" x1="0" y1="0" x2="1000" y2="1000" gradientUnits="userSpaceOnUse"/>
        <linearGradient xlink:href="#e" id="g" x1="0" y1="763.836" x2="1000" y2="763.836" gradientUnits="userSpaceOnUse"/>
        <filter style="color-interpolation-filters:sRGB" id="h" x="-.097" y="-.107" width="1.215" height="1.237">
            <feFlood result="flood" flood-opacity=".286" flood-color="#000"/>
            <feGaussianBlur result="blur" in="SourceGraphic" stdDeviation="20"/>
            <feOffset result="offset" in="blur" dx="10" dy="10"/>
            <feComposite result="comp1" operator="in" in="flood" in2="offset"/>
            <feComposite result="comp2" in="SourceGraphic" in2="comp1"/>
        </filter>
    </defs>
    <rect style="fill:url(#f);fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="1000" height="1000" ry="0"/>
    <rect style="fill:url(#g);fill-opacity:1;stroke-width:.485967;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:2.42983,4.3737;paint-order:markers stroke fill" width="1000" height="236.164" y="763.836" ry="0"/>
    <g transform="matrix(.9294 0 0 .9294 264.176 94.524)" style="filter:url(#h)">
        <path style="display:inline;fill:#3eac92" d="M312.127 292.149c10.88-28.608 18.982-61.79 18.982-97.175C331.11 87.293 256.073 0 256.073 0s-75.037 87.293-75.037 194.974c0 35.55 8.179 68.878 19.136 97.576v116.399l55.39 26.313 60.026-30.32z"/>
        <path style="display:inline;fill:#7cd8a4" d="M415.258 141.67s-52.248 13.736-80.934 55.34-22.949 95.322-22.949 95.322.634-.188.85-.248c-48.957 64.544-55.938 143.897-56.223 147.393-.284-3.48-7.237-82.49-55.898-146.961l1.521.445s5.737-53.718-22.95-95.322c-28.685-41.604-80.933-55.34-80.933-55.34s-4.456 41.874 14.242 80.315C59.093 197.666 9.807 193.926 9.807 193.926s7.742 102.516 75.746 170.522c67.733 67.735 169.565 75.666 170.377 75.728l-.002.018.082-.008.064.006-.002-.014c.812-.062 102.642-7.997 170.375-75.73 68.005-68.004 75.746-170.522 75.746-170.522s-48.727 3.687-101.277 28.256c18.81-38.495 14.342-80.512 14.342-80.512z"/>
        <path style="display:inline;opacity:.21;fill:#266659" d="M400.939 222.166c18.799-38.489 14.319-80.495 14.319-80.495s-37.863 9.96-66.823 38.59c-12.648 89.188-48.237 204.494-145.938 249.387 17.214 4.909 31.833 7.618 41.428 9.055l5.901 5.901c.232.32.483.63.772.918a7.513 7.513 0 0 0 5.329 2.207l.073-.003.073.003a7.515 7.515 0 0 0 5.329-2.207c.288-.288.54-.599.772-.918l5.901-5.901c29.127-4.363 104.552-20.434 158.373-74.255 68.004-68.004 75.745-170.522 75.745-170.522s-48.713 3.681-101.254 28.24z"/>
        <path style="display:inline;fill:#266659" d="M256.072 27.371c-4.162 0-7.535 3.395-7.535 7.583v107.603l-20.644-20.644a7.537 7.537 0 0 0-10.658 10.658l31.302 31.302v39.586l-20.644-20.646a7.537 7.537 0 0 0-10.658 10.658l31.302 31.303v39.576l-20.644-20.646a7.539 7.539 0 0 0-10.659 0 7.54 7.54 0 0 0 0 10.66l31.303 31.302v136.33l-52.76-52.76v-39.198a7.533 7.533 0 0 0-7.535-7.536 7.535 7.535 0 0 0-7.537 7.535v24.127l-23.38-23.38v-39.202a7.536 7.536 0 0 0-7.538-7.535 7.534 7.534 0 0 0-7.535 7.535v24.131l-23.389-23.388v-39.202a7.537 7.537 0 1 0-15.072 0v24.13l-56.738-56.739a7.513 7.513 0 0 0-5.328-2.207 7.537 7.537 0 0 0-5.33 12.865l56.738 56.739H69.002a7.537 7.537 0 1 0 0 15.072h39.203l23.387 23.387h-24.13a7.537 7.537 0 0 0-7.536 7.537 7.537 7.537 0 0 0 7.537 7.537h39.203l23.383 23.383h-24.131a7.537 7.537 0 1 0 0 15.072h39.203l64.824 64.824c.207.273.404.55.653.799a7.513 7.513 0 0 0 5.328 2.207c.025 0 .05-.008.074-.008.024 0 .048.008.072.008 1.93 0 3.86-.736 5.33-2.207.25-.249.446-.526.653-.799l64.824-64.824h39.201a7.536 7.536 0 1 0 0-15.072h-24.129l23.383-23.383h39.201a7.538 7.538 0 0 0 0-15.074h-24.127l23.387-23.387h39.201a7.536 7.536 0 1 0 0-15.072h-24.129l52.254-52.254a7.54 7.54 0 0 0 0-10.66 7.51 7.51 0 0 0-5.328-2.206 7.51 7.51 0 0 0-5.328 2.205l-52.258 52.258v-24.13a7.536 7.536 0 1 0-15.07 0v39.2l-23.39 23.391v-24.133a7.537 7.537 0 1 0-15.072 0v39.206l-23.382 23.38v-24.13a7.534 7.534 0 0 0-7.535-7.536 7.536 7.536 0 0 0-7.537 7.535v39.204l-52.612 52.609V285.666l31.301-31.302a7.536 7.536 0 1 0-10.656-10.66l-20.645 20.644v-39.574l31.301-31.303a7.537 7.537 0 0 0-10.656-10.658l-20.645 20.644v-39.584l31.301-31.302a7.537 7.537 0 0 0-10.656-10.658l-20.645 20.642V34.954c0-4.19-3.375-7.583-7.537-7.583zm141.424 132.497a7.53 7.53 0 0 0-6.281 3.26l-30.875 44.958-.738-4.013c-.752-4.094-4.682-6.795-8.776-6.05a7.533 7.533 0 0 0-6.049 8.774l3.473 18.893-25.842 37.627a7.537 7.537 0 0 0 12.41 8.558l25.916-37.738 18.711-3.437a7.533 7.533 0 0 0 6.05-8.774c-.753-4.094-4.678-6.797-8.774-6.05l-3.942.724 30.844-44.914a7.536 7.536 0 0 0-1.926-10.484 7.504 7.504 0 0 0-4.2-1.334zm-278.41 6.043a7.539 7.539 0 0 0-6.127 11.816l26.338 39.334-3.02-.555a7.537 7.537 0 0 0-2.723 14.826L151 234.538l26.338 39.333a7.527 7.527 0 0 0 6.21 3.258 7.539 7.539 0 0 0 6.197-11.816l-25.233-37.686 3.71-20.199a7.535 7.535 0 0 0-6.05-8.773c-4.086-.75-8.02 1.955-8.774 6.049l-.912 4.964-27.119-40.5a7.526 7.526 0 0 0-6.281-3.257z"/>
    </g>
    <g transform="matrix(.9294 0 0 .9294 37.404 -5.907)">
        <rect style="fill:#c3c3c3;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="55.908" height="185.136" x="665.326" y="358.862" ry="9.439"/>
        <path style="font-weight:600;font-size:31.3915px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Semi-Bold';letter-spacing:0;word-spacing:.840845px;fill:#303030;stroke-width:.840845;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:4.20422,7.5676;paint-order:markers stroke fill" d="M-498.627 704.173V682.2h4.08v21.974zm-15.445 0V682.2h4.081v21.974zm3.736-9.417v-3.485h12.023v3.485zm31.14 9.731q-4.52 0-7.094-2.542-2.543-2.543-2.543-7.346v-12.4h4.081v12.243q0 3.39 1.444 4.928 1.475 1.539 4.144 1.539 2.668 0 4.112-1.539 1.444-1.538 1.444-4.928v-12.243h4.018v12.4q0 4.803-2.574 7.346-2.543 2.542-7.032 2.542zm15.32-.314V682.2h3.358l9.606 16.041h-1.758l9.449-16.04h3.359l.031 21.973h-3.86l-.032-15.915h.816l-8.036 13.404h-1.821l-8.162-13.404h.942v15.915zm29.978 0V682.2h4.081v21.974zm10.014 0V682.2h9.606q3.579 0 6.278 1.382 2.7 1.38 4.207 3.83 1.507 2.448 1.507 5.775 0 3.296-1.507 5.776-1.507 2.449-4.207 3.83-2.7 1.381-6.278 1.381zm4.081-3.453h5.337q2.448 0 4.269-.941 1.82-.942 2.794-2.637 1.004-1.696 1.004-3.956 0-2.291-1.004-3.955-.973-1.695-2.794-2.637-1.82-.942-4.27-.942h-5.336zm22.1 3.673q-1.068 0-1.821-.722-.753-.753-.753-1.883 0-1.193.753-1.884.753-.722 1.82-.722 1.068 0 1.821.722.754.69.754 1.884 0 1.13-.754 1.883-.753.722-1.82.722z" transform="rotate(-90)" aria-label="HUMID."/>
    </g>
    <g transform="translate(244.838 480.474) scale(.50527)">
        <path style="fill:url(#i);fill-opacity:1;stroke-width:.949915;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:4.74957,8.54922;paint-order:markers stroke fill;filter:url(#filter75)" d="m48.832 129.242 141.44 542.778h619.456l141.44-542.778Z"/>
        <rect style="fill:url(#j);fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill;filter:url(#filter71)" width="1000" height="130.694" ry="27.724"/>
        <rect style="fill:url(#k);fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill;filter:url(#filter73)" width="685.419" height="123.434" x="157.29" y="670.898" ry="27.724"/>
    </g>
    <rect style="fill:url(#l);fill-opacity:1;stroke-width:.168834;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:.844169,1.51951;paint-order:markers stroke fill" width="1000" height="28.505" y="971.495" ry="0"/>
    <g transform="translate(0 -57.36)">
        <rect style="fill:#c3c3c3;fill-opacity:1;stroke-width:1.20175;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:6.00876,10.8158;paint-order:markers stroke fill" width="67.188" height="224.751" x="169.427" y="-287.892" ry="11.343" transform="rotate(90)"/>
        <rect style="fill:#c3c3c3;fill-opacity:1;stroke-width:1.20175;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:6.00876,10.8158;paint-order:markers stroke fill" width="67.188" height="223.724" x="260.302" y="-287.892" ry="11.343" transform="rotate(90)"/>
        <path style="font-weight:600;font-size:29.1751px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Semi-Bold';text-align:center;letter-spacing:0;word-spacing:.781477px;text-anchor:middle;fill:#303030;stroke-width:1.01049;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5.05242,9.09437;paint-order:markers stroke fill" d="M112.391 216.602q-3.018 0-5.62-.98-2.566-1.02-4.49-2.83-1.886-1.849-2.943-4.338-1.056-2.49-1.056-5.433 0-2.942 1.056-5.432 1.057-2.49 2.98-4.3 1.925-1.85 4.49-2.83 2.565-1.019 5.62-1.019 3.245 0 5.924 1.132 2.678 1.094 4.527 3.282l-3.17 2.98q-1.433-1.546-3.206-2.3-1.773-.793-3.848-.793t-3.81.679q-1.698.679-2.98 1.924-1.245 1.245-1.962 2.942-.679 1.698-.679 3.735t.679 3.735q.717 1.698 1.962 2.942 1.282 1.245 2.98 1.924 1.735.68 3.81.68t3.848-.755q1.773-.792 3.207-2.377l3.169 3.018q-1.849 2.15-4.527 3.282-2.679 1.132-5.96 1.132zm33.424-.377v-26.407h4.904v26.407zm-18.56 0v-26.407h4.904v26.407zm4.489-11.318v-4.187h14.448v4.187zm37.423 11.695q-5.433 0-8.526-3.056-3.056-3.055-3.056-8.827v-14.901h4.905v14.712q0 4.074 1.735 5.923 1.773 1.848 4.98 1.848 3.206 0 4.942-1.848 1.735-1.849 1.735-5.923v-14.713h4.829v14.902q0 5.772-3.094 8.827-3.056 3.056-8.45 3.056zm26.219-.377-11.544-26.407h5.319l10.299 23.88h-3.056l10.412-23.88h4.904l-11.506 26.407zm14.561 0 11.884-26.407h4.828l11.921 26.407h-5.13l-10.224-23.804h1.962l-10.186 23.804zm5.47-6.112 1.32-3.848h14.26l1.321 3.848z" aria-label="CHUVA"/>
        <path style="font-weight:600;font-size:29.1751px;line-height:1;font-family:Montserrat;-inkscape-font-specification:'Montserrat Semi-Bold';letter-spacing:0;word-spacing:.781477px;fill:#303030;stroke-width:1.01049;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5.05242,9.09437;paint-order:markers stroke fill" d="M108.562 307.1v-22.258H99.81v-4.15h22.408v4.15h-8.752v22.257zm17.353 0v-26.408h19.278v4.112H130.82v18.184h14.9v4.112zm4.527-11.393v-4.037h13.129v4.037zm20.749 11.392v-26.407h4.037l11.543 19.278h-2.112l11.355-19.278h4.036l.038 26.407h-4.64l-.038-19.126h.981l-9.657 16.109h-2.188l-9.809-16.109h1.132v19.126zm36.027 0v-26.407h10.865q3.508 0 5.998 1.132 2.528 1.132 3.886 3.244 1.358 2.113 1.358 5.018 0 2.904-1.358 5.017-1.358 2.113-3.886 3.244-2.49 1.132-5.998 1.132h-8.149l2.188-2.301v9.922zm4.904-9.393-2.188-2.377h7.922q3.245 0 4.867-1.358 1.66-1.396 1.66-3.885 0-2.528-1.66-3.886-1.622-1.358-4.867-1.358h-7.922l2.188-2.414zm22.484 9.658q-1.282 0-2.188-.868-.905-.905-.905-2.264 0-1.433.905-2.263.906-.868 2.188-.868 1.283 0 2.188.868.906.83.906 2.263 0 1.359-.906 2.264-.905.868-2.188.868z" aria-label="TEMP."/>
    </g>
    <rect style="fill:#303030;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="23.617" height="737.123" x="58.529" y="112.067" ry="6.418"/>
    <rect style="fill:#303030;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:5,9;paint-order:markers stroke fill" width="229.362" height="26.139" x="58.529" y="439.853" ry="6.418"/>
</svg>
"""


class Componente(QtWidgets.QWidget):
    def __init__(self, text:str = "", expressão: str = "False", parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet("""
            Componente QLabel {color: #fff; font-size: 25px; font-weight: bold;}
            QWidget#rectangle {background-color: #000; border-radius: 7px;}
            #ent1, #ent2, #ent3, #saida {background-color: #000; border-radius: 4px;}
            #saidaLed{border-radius: 15px;}
        """)
        self.setFixedSize(225, 128)

        self.expressão = expressão

        self.ents = [False, False, False]

        self.ent1 = QtWidgets.QFrame(parent=self)
        self.ent1.setObjectName("ent1")
        self.ent1.setFixedSize(30, 8)
        self.ent1.move(50, 10)
        self.btEnt1 = QtWidgets.QPushButton(parent=self, text="A: Off")
        self.btEnt1.setCursor(QtCore.Qt.PointingHandCursor)
        self.btEnt1.clicked.connect(lambda: self.setEnt(0))
        self.btEnt1.move(0, 0)

        self.ent2 = QtWidgets.QFrame(parent=self)
        self.ent2.setObjectName("ent2")
        self.ent2.setFixedSize(30, 8)
        self.ent2.move(50, 60)
        self.btEnt2 = QtWidgets.QPushButton(parent=self, text="B: Off")
        self.btEnt2.setCursor(QtCore.Qt.PointingHandCursor)
        self.btEnt2.clicked.connect(lambda: self.setEnt(1))
        self.btEnt2.move(0, 51)

        self.ent3 = QtWidgets.QFrame(parent=self)
        self.ent3.setObjectName("ent3")
        self.ent3.setFixedSize(30, 8)
        self.ent3.move(50, 110)
        self.btEnt3 = QtWidgets.QPushButton(parent=self, text="C: Off")
        self.btEnt3.setCursor(QtCore.Qt.PointingHandCursor)
        self.btEnt3.clicked.connect(lambda: self.setEnt(2))
        self.btEnt3.move(0, 101)

        self.btEnts = [self.btEnt1, self.btEnt2, self.btEnt3]

        self.saida = QtWidgets.QFrame(parent=self)
        self.saida.setObjectName("saida")
        self.saida.setFixedSize(30, 8)
        self.saida.move(170, 60)

        self.saidaLed = QtWidgets.QFrame(parent=self)
        self.saidaLed.setObjectName("saidaLed")
        self.saidaLed.setFixedSize(30, 30)
        self.saidaLed.setStyleSheet("background-color: #b0b0b0;")
        self.saidaLed.move(195, 48)

        self.rectangle = QtWidgets.QFrame(parent=self)
        self.rectangle.setObjectName("rectangle")
        self.rectangle.setFixedSize(100, 128)
        self.rectangle.move(75, 0)

        self.text = QtWidgets.QLabel(parent=self, text=text)
        self.text.setFixedSize(100, 128)
        self.text.move(75, 0)
        self.text.setAlignment(Qt.AlignCenter)
        
    @QtCore.Slot(int)
    def setEnt(self, ent:int):
        self.ents[ent] = not self.ents[ent]
        self.btEnts[ent].setText(f"{chr(65+ent)}: {'On' if self.ents[ent] else 'Off'}")
        # self.btEnts[ent].setStyleSheet("background-color: green;" if self.ents[ent] else "background-color: red;")

        A = self.ents[0]
        B = self.ents[1]
        C = self.ents[2]

        saída = eval(self.expressão)

        self.saidaLed.setStyleSheet("background-color: green;" if saída else "background-color: #b0b0b0;")


class Page1(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = [], position: list = []):
        super().__init__(parent)
        self.useHardware = False

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(60)

        for i, comp in enumerate(components, start=1):
            component = Componente(expressão=comp, text=str(i), parent=self)

            self.Layout.addWidget(component, *position[i-1])

class Page2(QtWidgets.QWidget):
    updateSignal = QtCore.Signal(list)
    setUseHardware = QtCore.Signal(bool)
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = []):
        super().__init__(parent)

        self.useHardware = False

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(20)

        self.image = QSvgWidget(parent=self)
        self.image.renderer().load(svg_Page3.encode("utf-8"))
        self.image.setFixedSize(400, 400)

        componentsItems = ["Hardware"]

        for i in range(len(components)):
            componentsItems.append(f"Componente {i+1}")

        self.ComboBox = QtWidgets.QComboBox(parent=self, placeholderText="Selecione um componente")
        self.ComboBox.addItems(componentsItems)
        self.ComboBox.setFixedHeight(32)
        self.ComboBox.setCursor(QtCore.Qt.PointingHandCursor)

        self.ComboBox.currentIndexChanged.connect(self.selectSimulation)

        self.Layout.addWidget(self.image, 0, 0)
        self.Layout.addWidget(self.ComboBox, 1, 0)

    @QtCore.Slot(int)
    def selectSimulation(self, index: int):
        if index == 0:
            self.useHardware = True
            self.setUseHardware.emit(True)
        else:
            self.useHardware = False
            self.setUseHardware.emit(False)
        pass

class Page3(QtWidgets.QWidget):
    updateSignal = QtCore.Signal(list)
    setUseHardware = QtCore.Signal(bool)
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = []):
        super().__init__(parent)

        self.useHardware = False

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(20)

        self.image = QSvgWidget(parent=self)
        self.image.renderer().load(svg_Page2.encode("utf-8"))
        self.image.setFixedSize(400, 400)

        componentsItems = ["Hardware"]

        for i in range(len(components)):
            componentsItems.append(f"Componente {i+1}")

        self.ComboBox = QtWidgets.QComboBox(parent=self, placeholderText="Selecione um componente")
        self.ComboBox.addItems(componentsItems)
        self.ComboBox.setFixedHeight(32)
        self.ComboBox.setCursor(QtCore.Qt.PointingHandCursor)

        self.ComboBox.currentIndexChanged.connect(self.selectSimulation)

        self.Layout.addWidget(self.image, 0, 0)
        self.Layout.addWidget(self.ComboBox, 1, 0)

    @QtCore.Slot(int)
    def selectSimulation(self, index: int):
        if index == 0:
            self.useHardware = True
            self.setUseHardware.emit(True)
        else:
            self.useHardware = False
            self.setUseHardware.emit(False)
        pass


class Projeto(QtWidgets.QWidget):
    updateSignal = QtCore.Signal()
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.useHardware = False
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.values = ["0","0","0","0","0","0","0","0","0","0"]

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(30)

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.Layout.addWidget(self.stackedWidget)

        comp1 = "A and (B or C)"
        comp2 = "A and not (B and C)"
        comp3 = "A or B or C"
        comp4 = "A and (B != C)"

        components = [comp1, comp2, comp3, comp4]
        position = [[0,0], [0,1], [1,0], [1,1]]

        self.page1 = Page1(components=components, position=position, parent=self.stackedWidget)
        self.page2 = Page2(parent=self.stackedWidget, components=components)
        self.page3 = Page3(parent=self.stackedWidget, components=components)

        self.page2.setUseHardware.connect(self.toggleUseHardware)
        self.page3.setUseHardware.connect(self.toggleUseHardware)

        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)
        self.stackedWidget.addWidget(self.page3)

        self.stackedWidget.setCurrentIndex(0)

        self.btTo2 = QtWidgets.QPushButton(parent=self, text="Próximo")
        self.btTo2.clicked.connect(self.nextPage)
        self.btTo2.setCursor(QtCore.Qt.PointingHandCursor)
        self.Layout.addWidget(self.btTo2)

    @Slot(bool)
    def toggleUseHardware(self, useHardware: bool):
        self.useHardware = useHardware
        pass

    @Slot()
    def nextPage(self):
        c = self.stackedWidget.currentIndex()
        count = self.stackedWidget.count() - 1

        if c < count:
            c = c+1
            self.stackedWidget.setCurrentIndex(c)
        else:
            c = 0
            self.stackedWidget.setCurrentIndex(c)

        self.useHardware = self.stackedWidget.currentWidget().useHardware

        if c == count:
            self.btTo2.setText("Voltar")
        else:
            self.btTo2.setText("Próximo")
        
        

    @Slot()
    def resetSimulation(self):
        pass

    @Slot(list)
    def updateSimulation(self, data: list):
        self.updateSignal.emit()
        pass

    @Slot()
    def getValues(self):
        self.values[0] = str(1)

        return self.values