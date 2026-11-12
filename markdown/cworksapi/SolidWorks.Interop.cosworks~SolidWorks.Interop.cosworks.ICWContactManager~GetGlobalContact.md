---
title: "GetGlobalContact Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "GetGlobalContact"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~GetGlobalContact.html"
---

# GetGlobalContact Method (ICWContactManager)

Gets the contact type and options for global contact.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetGlobalContact( _
   ByRef NContactType As System.Integer, _
   ByRef NOption As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim NContactType As System.Integer
Dim NOption As System.Integer

instance.GetGlobalContact(NContactType, NOption)
```

### C#

```csharp
void GetGlobalContact(
   out System.int NContactType,
   out System.int NOption
)
```

### C++/CLI

```cpp
void GetGlobalContact(
   [Out] System.int NContactType,
   [Out] System.int NOption
)
```

### Parameters

- `NContactType`: Type of global contact:

  - [static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies as defined in [swsContactSetTypeStaticNonLinear_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html)
  - [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies as defined in [swsContactSetTypeThermal_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeThermal_e.html)
  - [buckling](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html) and [frequency](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html) studies as defined [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html), excluding swsContactTypeStaticNoPenetration
- `NOption`: Mesh compatibility as defined in [swsMeshCompatibility_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshCompatibility_e.html)

## VBA Syntax

See [CWContactManager::GetGlobalContact](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~GetGlobalContact.html).

## Remarks

Contact set definitions override both global and component contact definitions. Component contact definitions override global contact definitions.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::SetGlobalContact Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~SetGlobalContact.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
