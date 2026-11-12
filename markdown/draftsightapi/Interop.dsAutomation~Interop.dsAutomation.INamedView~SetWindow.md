---
title: "SetWindow Method (INamedView)"
project: ""
interface: "INamedView"
member: "SetWindow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INamedView~SetWindow.html"
---

# SetWindow Method (INamedView)

Sets the window that defines the named view.

## Syntax

### Visual Basic

```vb
Sub SetWindow( _
   ByVal FirstCorner As MathPoint, _
   ByVal OppositeCorner As MathPoint _
)
```

### C#

```csharp
void SetWindow(
   MathPoint FirstCorner,
   MathPoint OppositeCorner
)
```

### JScript

```
function SetWindow(
   FirstCorner : MathPoint,
   OppositeCorner : MathPoint
);
```

### Managed Extensions for C++

```
void SetWindow(
   MathPoint* FirstCorner,
   MathPoint* OppositeCorner
)
```

### C++/CLI

```cpp
void SetWindow(
   MathPoint^ FirstCorner,
   MathPoint^ OppositeCorner
)
```

### Parameters

- `FirstCorner`: Corner [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) of the window that defines the named view
- `OppositeCorner`: Corner [point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html) opposite FirstCorner that defines the named view

## See Also

[INamedView Interface](Interop.dsAutomation~Interop.dsAutomation.INamedView.html)
[INamedView Members](Interop.dsAutomation~Interop.dsAutomation.INamedView_members.html)
[INamedView::GetName Method ()](Interop.dsAutomation~Interop.dsAutomation.INamedView~GetName.html)

## Availability

DraftSight V1R5.0
