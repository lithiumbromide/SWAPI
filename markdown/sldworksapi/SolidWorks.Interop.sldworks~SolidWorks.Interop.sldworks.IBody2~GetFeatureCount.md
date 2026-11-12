---
title: "GetFeatureCount Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetFeatureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFeatureCount.html"
---

# GetFeatureCount Method (IBody2)

Gets the number of features in this body in a multibody sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Integer

value = instance.GetFeatureCount()
```

### C#

```csharp
System.int GetFeatureCount()
```

### C++/CLI

```cpp
System.int GetFeatureCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of features in this body

## VBA Syntax

See [Body2::GetFeatureCount](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetFeatureCount.html).

## Examples

[Get Features of Multibody Sheet Metal Part (C#)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_CSharp.htm)
[Get Features of Multibody Sheet Metal Part (VB.NET)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_VBNET.htm)
[Get Features of Multibody Sheet Metal Part (VBA)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_VB.htm)

## Remarks

The features of a body in a multibody sheet metal part are located in the solid bodies folder in the FeatureManager design tree.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFeatures.html)
[IBody2::IGetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFeatures.html)
[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder::GetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodies.html)
[IBodyFolder::GetBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodyCount.html)
[IBodyFolder::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~IGetBodies.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
