import React, { useState } from 'react';
import Carousel from 'react-bootstrap/Carousel';
import classes from './AllInput.module.css';
import Grid from '@mui/material/Grid';

export function AllInputPage() {
  const RadioInput = ({ value, checked, setter }) => {
    return (
      <label className={classes.detail_input}>
        <input
          className={classes.hidden}
          type="radio"
          checked={checked === value}
          onChange={() => setter(value)}
        />
        <span className={classes.detail_label} />
      </label>
    );
  };
  const RadioInputSet = ({ checked, setter }) => {
    return (
      <div id="radios">
        <RadioInput value="1" checked={checked} setter={setter} />
        <RadioInput value="2" checked={checked} setter={setter} />
        <RadioInput value="3" checked={checked} setter={setter} />
        <RadioInput value="4" checked={checked} setter={setter} />
        <RadioInput value="5" checked={checked} setter={setter} />
      </div>
    );
  };
  const [index, setIndex] = useState(0);
  const handleSelect = (selectedIndex, e) => {
    setIndex(selectedIndex);
  };
  const [outpatient, setOutpatient] = useState('3');
  const [hospitalization, setHospitalization] = useState('3');
  const [operation, setOperation] = useState('3');
  const [patella, setPatella] = useState('3');
  const [skin, setSkin] = useState('3');
  const [dental, setDental] = useState('3');
  const [urinary, setUrinary] = useState('3');
  const [liability, setLiability] = useState('3');
  const handleSubmit = e => {
    e.preventDefault();
    const data = {
      outpatient,
      hospitalization,
      operation,
      patella,
      skin,
      dental,
      urinary,
      liability,
    };
    const json = JSON.stringify(data, null, 16);
    console.log(json);
  };
  return (
    <Grid container direction="column" justifyContent="center" alignItems="center">
      <div style={{ height: 900 }}>
        <form onSubmit={handleSubmit} style={{ marginTop: 30 }}>
          <Carousel
            activeIndex={index}
            onSelect={handleSelect}
            interval={null}
            style={{ width: 1000 }}
          >
            <Carousel.Item>
              <img
                className="d-block w-100"
                src={`${process.env.PUBLIC_URL}/detail_survey/1.png`}
                alt="First slide"
              />
              <Carousel.Caption style={{ color: '#000' }}>
                <div>
                  <label>통원치료비 : </label>
                  <RadioInputSet checked={outpatient} setter={setOutpatient} />
                </div>
                <div>
                  <label>입원치료비 : </label>
                  <RadioInputSet checked={hospitalization} setter={setHospitalization} />
                </div>
                <div>
                  <label>수술치료비 : </label>
                  <RadioInputSet checked={operation} setter={setOperation} />
                </div>
              </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
              <img
                className="d-block w-100"
                src={`${process.env.PUBLIC_URL}/detail_survey/2.svg`}
                alt="Second slide"
              />
              <Carousel.Caption style={{ color: '#000', right: '10%', left: '10%' }}>
                <div>
                  <span>슬개골치료 : </span>
                  <RadioInputSet checked={patella} setter={setPatella} />
                </div>
                <div>
                  <span>피부병 : </span>
                  <RadioInputSet checked={skin} setter={setSkin} />
                </div>
                <div>
                  <span>구강 / 치과 : </span>
                  <RadioInputSet checked={dental} setter={setDental} />
                </div>
                <div>
                  <span>비뇨기 : </span>
                  <RadioInputSet checked={urinary} setter={setUrinary} />
                </div>
                <div>
                  <label>배상책임 : </label>
                  <RadioInputSet checked={liability} setter={setLiability} />
                </div>
                <div>
                  <a className={classes.allinputSubmit}>설문 제출 후, 상세 검색 바로가기</a>
                </div>
              </Carousel.Caption>
            </Carousel.Item>
          </Carousel>
        </form>
      </div>
    </Grid>
  );
}
