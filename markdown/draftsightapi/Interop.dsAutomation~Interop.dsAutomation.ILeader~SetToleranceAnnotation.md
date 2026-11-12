---
title: "SetToleranceAnnotation Method (ILeader)"
project: ""
interface: "ILeader"
member: "SetToleranceAnnotation"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~SetToleranceAnnotation.html"
---

# SetToleranceAnnotation Method (ILeader)

Attaches a [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) to the Leader.

## Syntax

### Visual Basic

```vb
Sub SetToleranceAnnotation( _
   ByVal ToleranceText As System.String, _
   ByVal InsertPoint As MathPoint _
)
```

### C#

```csharp
void SetToleranceAnnotation(
   System.string ToleranceText,
   MathPoint InsertPoint
)
```

### JScript

```
function SetToleranceAnnotation(
   ToleranceText : System.String,
   InsertPoint : MathPoint
);
```

### Managed Extensions for C++

```
void SetToleranceAnnotation(
   System.string* ToleranceText,
   MathPoint* InsertPoint
)
```

### C++/CLI

```cpp
void SetToleranceAnnotation(
   System.String^ ToleranceText,
   MathPoint^ InsertPoint
)
```

### Parameters

- `ToleranceText`: Text for the geometric Tolerance to attach to the Leader
- `InsertPoint`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) where to insert the geometric Tolerance to the Leader

## Examples

[Attach Note and Tolerance Annotations to Leaders (C#)](Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_CSharp.htm)
[Attach Note and Tolerance Annotations to Leaders (VB.NET)](Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_VBNET.htm)
[Attach Note and Tolerance Annotations to Leaders (VBA)](Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_VBA.htm)
[Attach Note and Tolerance Annotations to Leaders (JavaScript)](Attach_Note_and_Tolerance_Annotations_to_Leaders_Example_JS.htm)

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)
[ILeader::GetToleranceAnnotation Method](Interop.dsAutomation~Interop.dsAutomation.ILeader~GetToleranceAnnotation.html)
[ILeader::RemoveAnnotation Method](Interop.dsAutomation~Interop.dsAutomation.ILeader~RemoveAnnotation.html)

## Availability

DraftSight V1R3.1
