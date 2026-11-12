---
title: "InitializeHole Method (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "InitializeHole"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~InitializeHole.html"
---

# InitializeHole Method (IWizardHoleFeatureData2)

Initializes a newly created Hole Wizard feature data object.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InitializeHole( _
   ByVal GenericHoleType As System.Integer, _
   ByVal StdIndex As System.Integer, _
   ByVal FastnerType As System.Integer, _
   ByVal SSize As System.String, _
   ByVal EndType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim GenericHoleType As System.Integer
Dim StdIndex As System.Integer
Dim FastnerType As System.Integer
Dim SSize As System.String
Dim EndType As System.Integer

instance.InitializeHole(GenericHoleType, StdIndex, FastnerType, SSize, EndType)
```

### C#

```csharp
void InitializeHole(
   System.int GenericHoleType,
   System.int StdIndex,
   System.int FastnerType,
   System.string SSize,
   System.int EndType
)
```

### C++/CLI

```cpp
void InitializeHole(
   System.int GenericHoleType,
   System.int StdIndex,
   System.int FastnerType,
   System.String^ SSize,
   System.int EndType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GenericHoleType`: Hole type as defined in [swWzdGeneralHoleTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdGeneralHoleTypes_e.html)
- `StdIndex`: Standard as defined in [swWzdHoleStandards_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandards_e.html)
- `FastnerType`: Screw type as defined in [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)
- `SSize`: Size of the hole
- `EndType`: End type as defined in [swEndConditions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

## VBA Syntax

See [WizardHoleFeatureData2::InitializeHole](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~InitializeHole.html).

## Remarks

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
