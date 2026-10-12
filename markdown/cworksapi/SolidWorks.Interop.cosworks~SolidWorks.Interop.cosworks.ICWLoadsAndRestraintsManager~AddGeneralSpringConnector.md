---
title: "AddGeneralSpringConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddGeneralSpringConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddGeneralSpringConnector.html"
---

# AddGeneralSpringConnector Method (ICWLoadsAndRestraintsManager)

Adds a general spring connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddGeneralSpringConnector( _
   ByVal DispFaceComp1 As System.Object, _
   ByVal DispFaceComp2 As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWGeneralSpringConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim DispFaceComp1 As System.Object
Dim DispFaceComp2 As System.Object
Dim ErrorCode As System.Integer
Dim value As CWGeneralSpringConnector

value = instance.AddGeneralSpringConnector(DispFaceComp1, DispFaceComp2, ErrorCode)
```

### C#

```csharp
CWGeneralSpringConnector AddGeneralSpringConnector(
   System.object DispFaceComp1,
   System.object DispFaceComp2,
   ref System.int ErrorCode
)
```

### C++/CLI

```cpp
CWGeneralSpringConnector^ AddGeneralSpringConnector(
   System.Object^ DispFaceComp1,
   System.Object^ DispFaceComp2,
   System.int% ErrorCode
)
```

### Parameters

- `DispFaceComp1`: Component 1 face
- `DispFaceComp2`: Component 2 face
- `ErrorCode`: Error code as defined by [swsGeneralSpringError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsGeneralSpringError_e.html)

### Return Value

[General spring connector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddGeneralSpringConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddGeneralSpringConnector.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::GetGeneralSpringConnector Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetGeneralSpringConnector.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
