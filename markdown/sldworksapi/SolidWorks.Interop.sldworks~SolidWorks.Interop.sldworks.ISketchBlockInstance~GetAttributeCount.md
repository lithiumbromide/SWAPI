---
title: "GetAttributeCount Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "GetAttributeCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeCount.html"
---

# GetAttributeCount Method (ISketchBlockInstance)

Gets the number of attributes for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttributeCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Integer

value = instance.GetAttributeCount()
```

### C#

```csharp
System.int GetAttributeCount()
```

### C++/CLI

```cpp
System.int GetAttributeCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of attributes

## VBA Syntax

See [SketchBlockInstance::GetAttributeCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~GetAttributeCount.html).

## Remarks

Attributes are notes that have tag names and are not read-only.

Call this method before before calling [ISketchBlockInstance::IGetAttributes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~IGetAttributes.html) to get the size of the array for that method.

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::GetAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributes.html)
[ISketchBlockInstance::GetAttributeValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.html)
[ISketchBlockInstance::SetAttributeValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
