---
title: "GetDefinitionTransform Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetDefinitionTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetDefinitionTransform.html"
---

# GetDefinitionTransform Method (IDisplayDimension)

Gets the transform for this dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefinitionTransform() As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As MathTransform

value = instance.GetDefinitionTransform()
```

### C#

```csharp
MathTransform GetDefinitionTransform()
```

### C++/CLI

```cpp
MathTransform^ GetDefinitionTransform();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) object

## VBA Syntax

See [DisplayDimension::GetDefinitionTransform](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetDefinitionTransform.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12.2
