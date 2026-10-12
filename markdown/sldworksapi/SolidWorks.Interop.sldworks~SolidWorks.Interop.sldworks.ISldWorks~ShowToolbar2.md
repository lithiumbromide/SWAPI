---
title: "ShowToolbar2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ShowToolbar2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowToolbar2.html"
---

# ShowToolbar2 Method (ISldWorks)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowToolbar2( _
   ByVal Cookie As System.Integer, _
   ByVal ToolbarId As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim ToolbarId As System.Integer
Dim value As System.Boolean

value = instance.ShowToolbar2(Cookie, ToolbarId)
```

### C#

```csharp
System.bool ShowToolbar2(
   System.int Cookie,
   System.int ToolbarId
)
```

### C++/CLI

```cpp
System.bool ShowToolbar2(
   System.int Cookie,
   System.int ToolbarId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`:
- `ToolbarId`:

## VBA Syntax

See [SldWorks::ShowToolbar2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ShowToolbar2.html).

## Remarks

SOLIDWORKS manages the display of the toolbars based on the user's action; therefore, this method is not needed. There are no alternative methods available to use.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
