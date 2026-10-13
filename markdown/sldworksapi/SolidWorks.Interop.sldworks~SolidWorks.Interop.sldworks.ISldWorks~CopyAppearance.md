---
title: "CopyAppearance Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CopyAppearance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyAppearance.html"
---

# CopyAppearance Method (ISldWorks)

Copies the appearance of the specified entity to the clipboard.

## Syntax

### Visual Basic (Declaration)

```vb
Function CopyAppearance( _
   ByVal Object As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Object As System.Object
Dim value As System.Boolean

value = instance.CopyAppearance(Object)
```

### C#

```csharp
System.bool CopyAppearance(
   System.object Object
)
```

### C++/CLI

```cpp
System.bool CopyAppearance(
   System.Object^ Object
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Object`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html), [component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html), or [part](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) whose appearance you want to copy

### Return Value

True if appearance is successfully copied to the clipboard, false if not

## VBA Syntax

See [SldWorks::CopyAppearance](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CopyAppearance.html).

## Examples

[Copy and Paste Appearances (VBA)](Copy_and_Paste_Appearances_Example_VB.htm)
[Copy and Paste Appearances (VB.NET)](Copy_and_Paste_Appearances_Example_VBNET.htm)
[Copy and Paste Appearances (C#)](Copy_and_Paste_Appearances_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::PasteAppearance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PasteAppearance.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
