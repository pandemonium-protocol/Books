\documentclass{article}
\usepackage{tikz}
\usepackage[margin=0in, paperwidth=15cm, paperheight=15cm]{geometry}

\begin{document}
\thispagestyle{empty}
\mbox{}

\begin{tikzpicture}[remember picture, overlay]
    % --- SCALING & CENTERING ---
    \pgfmathsetmacro{\modsize}{0.1 * \paperwidth / 22}
    \pgfmathsetmacro{\buffer}{28.45}
    \pgfmathsetmacro{\offsetX}{\paperwidth - 23 * \modsize - \buffer}
    \pgfmathsetmacro{\offsetY}{\paperheight - 25 * \modsize - \buffer}

    % --- 21x21 STANDARD QR DATA ---
    \foreach \val [count=\i] in {
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, % Pad
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, % Pad
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, % Pad
        1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0, % Row 1
        1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,1,0,
        1,0,1,1,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1,0,1,0,
        1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,1,1,0,1,0,
        1,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,1,0,
        1,0,0,0,0,0,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,0,
        1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,
        0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,
        1,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,
        1,0,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,
        1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,0,0,
        0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,
        0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,0,
        0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,
        1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1,0,0,
        1,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,1,1,0,
        1,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,0,
        1,0,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,
        1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,
        1,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,
        1,1,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,0,1,0,0  % Row 21
    }{
        \pgfmathtruncatemacro{\row}{(\i-1)/22}
        \pgfmathtruncatemacro{\col}{mod(\i-1,22)}
        
        \ifnum\val=1
            \fill[black] ([xshift=\col*\modsize pt + \offsetX pt, yshift=-\row*\modsize pt - \offsetY pt]current page.north west) 
            rectangle ++(\modsize pt, -\modsize pt);
        \fi
    }
\end{tikzpicture}

\end{document}
```

Standard Version 1 QR — every phone camera should pick this up. Same lower-right positioning with the 1cm print-safe buffer.
