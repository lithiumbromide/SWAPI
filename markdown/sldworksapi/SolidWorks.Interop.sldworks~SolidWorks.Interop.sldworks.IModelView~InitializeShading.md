---
title: "InitializeShading Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "InitializeShading"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~InitializeShading.html"
---

# InitializeShading Method (IModelView)

Sets up the model view for OpenGL shading.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InitializeShading()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView

instance.InitializeShading()
```

### C#

```csharp
void InitializeShading()
```

### C++/CLI

```cpp
void InitializeShading();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelView::InitializeShading](ms-its:sldworksapivb6.chm::/sldworks~ModelView~InitializeShading.html).

## Remarks

Third-party developers should call this method if they are going to use OpenGL shading and are unsure whether shading has already been used for the current window. This method needs to be called for any window drawn into with OpenGL calls.

This method is provided so third-party applications do not need to use any of the Choos...() functions provided in the OpenGL library. Many of the Choos..() functions, for example ChoosePixelFormat(), can only be called once per window. In the case of ChoosePixelFormat(), a second call to the function is ignored. The effect is harmless if the third-party application makes this call after the SOLIDWORKS Design application has made the call. However, it is dangerous if the third party were to call it first because the SOLIDWORKS Design application may require a more complicated format.

To make OpenGL calls, you must get an OpenGL render context (RC). We keep our render context private so that there are not any problems with corruption of SOLIDWORKS RC by an application. To get a rendering context to make OpenGL calls, you must:

```vb
uiModelView_c::InitializeShading()
CClientDC dC(CWnd* parentWindow);
HGLRC hRc = ::wglCreateContext(dC.m_hDC);
::wglMakeCurrent(dC.m_hDC, hRc); (call this before each 'paint' operation)
```

When you are done using OpenGL for this paint'operation, call:

```vb
::wglMakeCurrent(NULL, NULL);
```

When the DLL shuts down or the [IModelView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) object is destroyed (watch for a [DModelViewEvents DestroyNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_DestroyNotify2EventHandler.html)), your application must do the following:

```vb
::wglMakeCurrent(NULL, NULL);
::wglDeleteContext(hRc);
```

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelDoc2::ViewOglShading Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewOglShading.html)
