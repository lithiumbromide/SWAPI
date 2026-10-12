---
title: "GetWhatsWrongCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetWhatsWrongCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrongCount.html"
---

# GetWhatsWrongCount Method (IModelDocExtension)

Gets the number of items in the What's Wrong dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWhatsWrongCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.GetWhatsWrongCount()
```

### C#

```csharp
System.int GetWhatsWrongCount()
```

### C++/CLI

```cpp
System.int GetWhatsWrongCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of items in the What's Wrong dialog

## VBA Syntax

See [ModelDocExtension::GetWhatsWrongCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetWhatsWrongCount.html).

## Examples

[Get What's Wrong (C#)](Get_What's_Wrong_Example_CSharp.htm)
[Get What's Wrong (VB.NET)](Get_What's_Wrong_Example_VBNET.htm)
[Get What's Wrong (VBA)](Get_What's_Wrong_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IFeature::GetErrorCode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.html)
[IModelDocExtension::GetWhatsWrong Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrong.html)

## Availability

SOLIDWORKS 2009 SP3, Revision Number 17.3
