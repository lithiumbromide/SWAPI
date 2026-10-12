---
title: "CreateContactComponent Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "CreateContactComponent"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactComponent.html"
---

# CreateContactComponent Method (ICWContactManager)

Creates the specified component contact.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateContactComponent( _
   ByVal NContactType As System.Integer, _
   ByVal NOption As System.Integer, _
   ByVal DispEntity As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWContactComponent
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim NContactType As System.Integer
Dim NOption As System.Integer
Dim DispEntity As System.Object
Dim ErrorCode As System.Integer
Dim value As CWContactComponent

value = instance.CreateContactComponent(NContactType, NOption, DispEntity, ErrorCode)
```

### C#

```csharp
CWContactComponent CreateContactComponent(
   System.int NContactType,
   System.int NOption,
   System.object DispEntity,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWContactComponent^ CreateContactComponent(
   System.int NContactType,
   System.int NOption,
   System.Object^ DispEntity,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NContactType`: Type of component contact for:

  - [static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html), [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html), [buckling](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html) and [thermal](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html) studies as defined in [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html)
  - [frequency](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html) studies as defined in [swsContactType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsContactType_e.html), excluding swsContactTypeStaticNoPenetration
- `NOption`: Mesh compatibility as defined in [swsMeshCompatibility_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMeshCompatibility_e.html)
- `DispEntity`: Component entity
- `ErrorCode`: Error code as defined in [swsContactComponentEndEditError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactComponentEndEditError_e.html)

### Return Value

[Component contact](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactComponent.html)

## VBA Syntax

See [CWContactManager::CreateContactComponent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~CreateContactComponent.html).

## Examples

[Add Component Contacts (VBA)](Add_Component_Contacts_Example_VB.htm)
[Add Component Contacts (VB.NET)](Add_Component_Contacts_Example_VBNET.htm)
[Add Component Contacts (C#)](Add_Component_Contacts_Example_CSharp.htm)

## Remarks

See the SOLIDWORKS Simulation Help for guidelines about studies with contact conditions.

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::DeleteContactComponent Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~DeleteContactComponent.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
