---
title: "InsertIndent Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertIndent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertIndent.html"
---

# InsertIndent Method (IFeatureManager)

Inserts an indent feature using a selected target body and tool body regions.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertIndent( _
   ByVal Thickness As System.Double, _
   ByVal Clearance As System.Double, _
   ByVal Exclude As System.Boolean, _
   ByVal ClrDir As System.Boolean, _
   ByVal Cut As System.Boolean, _
   ByVal CutDir As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Thickness As System.Double
Dim Clearance As System.Double
Dim Exclude As System.Boolean
Dim ClrDir As System.Boolean
Dim Cut As System.Boolean
Dim CutDir As System.Boolean
Dim value As Feature

value = instance.InsertIndent(Thickness, Clearance, Exclude, ClrDir, Cut, CutDir)
```

### C#

```csharp
Feature InsertIndent(
   System.double Thickness,
   System.double Clearance,
   System.bool Exclude,
   System.bool ClrDir,
   System.bool Cut,
   System.bool CutDir
)
```

### C++/CLI

```cpp
Feature^ InsertIndent(
   System.double Thickness,
   System.double Clearance,
   System.bool Exclude,
   System.bool ClrDir,
   System.bool Cut,
   System.bool CutDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Thickness of the indent feature
- `Clearance`: Distance between the tool body and target body (see **Remarks**)
- `Exclude`: True to exclude the selections, false to include the selections
- `ClrDir`: True to leave the direction of clearance as is, false to reverse the direction of the clearance
- `Cut`: True to cut the target body, false to not
- `CutDir`: True to reverse the direction of the cut if the tool body is a surface, false to not

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertIndent](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertIndent.html).

## Examples

[Insert Indent Feature (C#)](Insert_Indent_Feature_Example_CSharp.htm)
[Insert Indent Feature (VB.NET)](Insert_Indent_Feature_Example_VBNET.htm)
[Insert Indent Feature (VBA)](Insert_Indent_Feature_Example_VB.htm)

## Remarks

Prior to calling this method, you must have selected the target body and tool body regions, using these selection marks:

- Target body = 1
- Tool body region = 4

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
