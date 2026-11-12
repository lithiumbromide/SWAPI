---
title: "SetGlobalContact Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "SetGlobalContact"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~SetGlobalContact.html"
---

# SetGlobalContact Method (ICWContactManager)

Sets the contact type and options for global contacts.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetGlobalContact( _
   ByVal NContactType As System.Integer, _
   ByVal NOption As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim NContactType As System.Integer
Dim NOption As System.Integer

instance.SetGlobalContact(NContactType, NOption)
```

### C#

```csharp
void SetGlobalContact(
   System.int NContactType,
   System.int NOption
)
```

### C++/CLI

```cpp
void SetGlobalContact(
   System.int NContactType,
   System.int NOption
)
```

### Parameters

- `NContactType`: Type global contact:

  - [static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies as defined in [swsContactSetTypeStaticNonLinear_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html)
  - [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies as defined in [swsContactSetTypeThermal_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactSetTypeThermal_e.html)
  - [buckling](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html) and [frequency](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html) studies as defined [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html), excluding swsContactTypeStaticNoPenetration
- `NOption`: Mesh compatibility as defined in [swsMeshCompatibility_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshCompatibility_e.html)

## VBA Syntax

See [CWContactManager::SetGlobalContact](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~SetGlobalContact.html).

## Remarks

Contact set definitions override both global and component contact definitions. Component contact definitions override global contact definitions.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::GetGlobalContact Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~GetGlobalContact.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
