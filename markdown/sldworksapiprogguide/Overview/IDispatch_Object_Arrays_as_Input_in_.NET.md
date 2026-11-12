---
title: "IDispatch Object Arrays as Input in .NET"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/IDispatch_Object_Arrays_as_Input_in_.NET.htm"
---

# IDispatch Object Arrays as Input in .NET

In the .NET Framework, an object array can be used to store System.Object types like integer, double, etc. .NET marshals these data types automatically. However, non-standard object types like SOLIDWORKS interfaces must be explicitly marshaled to an IDispatch object array.

Some SOLIDWORKS methods and properties have input arrays of non-standard objects. Before passing these arrays, you must marshal them to IDispatch object arrays using the System.Runtime.InteropServices.DispatchWrapper class.

Several SOLIDWORKS methods and properties have input object arrays that must be marshaled to an IDispatch object array. The following Help topics contain links to VB.NET and C# examples that demonstrate how to marshal an array of non-standard input objects to an IDispatch object array.

- [IAssemblyDoc::CopyWithMates](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAssemblyDoc~CopyWithMates.html)
- [IAssemblyDoc::ReorderComponents](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAssemblyDoc~ReorderComponents.html)
- [IExportPDFData::SetSheets](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IExportPDFData~SetSheets.html)
- [ILibraryFeatureData::SetReferences](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ILibraryFeatureData~SetReferences.html)
- [ISheet::InsertTitleBlock](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISheet~InserttitleBlock.html)
- [IView::Bodies](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~Bodies.html)
