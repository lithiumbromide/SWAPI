---
title: "InstallModelColorizer Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InstallModelColorizer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InstallModelColorizer.html"
---

# InstallModelColorizer Method (IModelDocExtension)

Installs your implemented interface of the [ISwColorContour](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour.html) interface.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InstallModelColorizer( _
   ByVal PInterface As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PInterface As System.Object

instance.InstallModelColorizer(PInterface)
```

### C#

```csharp
void InstallModelColorizer(
   System.object PInterface
)
```

### C++/CLI

```cpp
void InstallModelColorizer(
   System.Object^ PInterface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PInterface`: Pointer to your implemented interface

## VBA Syntax

See [ModelDocExtension::InstallModelColorizer](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InstallModelColorizer.html).

## Remarks

After your implemented interface is installed, the SOLIDWORKS Design software calls [ISwColorContour::Value](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour~Value.html) on each graphical update. Your implemented interface must provide the corresponding color for each vertex and the value associated with each vertex. This value is displayed when the cursor is over that vertex.

Additionally, when the cursor is over the model, the SOLIDWORKS Design software calls [ISwColorContour::DisplayString](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour~DisplayString.html) and passes the value to be formatted by your implemented interface, which the SOLIDWORKS Design software will then display.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::RemoveModelColorizer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveModelColorizer.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
