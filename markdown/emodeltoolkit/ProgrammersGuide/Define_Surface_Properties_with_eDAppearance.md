---
title: "Define Surface Properties with eDAppearance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "emodeltoolkit/ProgrammersGuide/Define_Surface_Properties_with_eDAppearance.htm"
---

# Define Surface Properties with eDAppearance

When creating a [eDPart](../eDPart/eDPart_Class.htm), [eDAssembly](../eDAssembly/eDAssembly_Class.htm), [eDBody](../eDBody/eDBody_Class.htm), [eDCurvleList](../eDCurveList/eDCurveList_Class.htm), [eDShellList](../eDShellList/eDShellList_Class.htm), or [eDMarkerList](../eDMarkerList/eDMarkerList_Class.htm), you apply the [eDAppearance](../eDAppearance/eDAppearance_Class.htm) object to it.

The lowest level object's appearance overrides all higher level objects' appearances. For example, a body specified as red that contains a face specified as blue and an edge with no specification will render a blue face and a red edge.
