---
title: "PreviewRequestHandler Delegate (SolidWorks.Visualize.Interfaces)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "PreviewRequestHandler"
member: ""
kind: "topic"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.PreviewRequestHandler.html"
---

# PreviewRequestHandler Delegate (SolidWorks.Visualize.Interfaces)

Obsolete. Handles preview requests.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub PreviewRequestHandler( _
   ByVal w As System.Integer, _
   ByVal h As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New PreviewRequestHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void PreviewRequestHandler(
   System.int w,
   System.int h
)
```

### C++/CLI

```cpp
public delegate void PreviewRequestHandler(
   System.int w,
   System.int h
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

### Parameters

- `w`: Width of the requested image
- `h`: Height of the requested image

## Examples

See the [IRenderNotificationHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html) example.

## Remarks

Users of the SOLIDWORKS Visualize API can request preview images of an on-going render.

Please note that requesting very large preview images can negatively impact the performance of the on-going render.

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
