---
title: "GetSelectionsCount Method (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "GetSelectionsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~GetSelectionsCount.html"
---

# GetSelectionsCount Method (IRefPlaneFeatureData)

Gets the number of entities selected to create this reference plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim value As System.Integer

value = instance.GetSelectionsCount()
```

### C#

```csharp
System.int GetSelectionsCount()
```

### C++/CLI

```cpp
System.int GetSelectionsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities selected to create this reference plane feature

## VBA Syntax

See [RefPlaneFeatureData::GetSelectionsCount](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~GetSelectionsCount.html).

## Remarks

Call this method before calling [IRefPlaneFeatureData::IGetSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData~IGetSelections.html).

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[IRefPlaneFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ISetSelections.html)
[IRefPlaneFeatureData::Selections Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Selections.html)
[IRefPlaneFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ISetSelections.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
