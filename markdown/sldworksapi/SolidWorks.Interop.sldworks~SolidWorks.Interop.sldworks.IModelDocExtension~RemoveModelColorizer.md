---
title: "RemoveModelColorizer Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "RemoveModelColorizer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveModelColorizer.html"
---

# RemoveModelColorizer Method (IModelDocExtension)

Removes your installed implemented interface of the [ISwColorContour](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour.html) interface.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveModelColorizer( _
   ByVal PInterface As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PInterface As System.Object

instance.RemoveModelColorizer(PInterface)
```

### C#

```csharp
void RemoveModelColorizer(
   System.object PInterface
)
```

### C++/CLI

```cpp
void RemoveModelColorizer(
   System.Object^ PInterface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PInterface`: Pointer to your installed implemented interface

## VBA Syntax

See [ModelDocExtension::RemoveModelColorizer](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~RemoveModelColorizer.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::InstallModelColorizer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InstallModelColorizer.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
